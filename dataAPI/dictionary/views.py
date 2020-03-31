from django.shortcuts import render,HttpResponse
from dictionary import models
from django.db import connection
import pymysql
import json
from django.core.serializers.json import DjangoJSONEncoder
from dictionary import dbConn

# import sys
#
# sys.setrecursionlimit(1000000)
# Create your views here.

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def getSqlDicRes(sql):
    "提取后台数据库数据"
    with connection.cursor() as cursor:
        cursor.execute(sql)
    sql_result = dictfetchall(cursor)
    return sql_result

def getConfigInfo(sql = '''SELECT dcd.id,dcd.sys_name,dcd.fetch_method,dcd.table_name,dcd.remark AS rm1, 
                 dcs.type, dcs.src_url, dcs.host, dcs.port, dcs.user, dcs.pwd, dcs.charset, dcs.remark AS rm2 
                 FROM dictionary_configdata AS dcd 
                 LEFT JOIN dictionary_configsrc AS dcs 
                 ON dcd.name_id = dcs.id;'''):
    return getSqlDicRes(sql)

def getTableInfo(connInfo):
    tableInfo = []
    for conn in connInfo:
        temp_info = {}
        for item in conn:
            if item == 'id' or item == 'table_name' or item =='rm1':
                temp_info[item]=conn.get(item)
        if conn.get('type') == "mysql数据源":
            dbConnection = dbConn.mysql(
                host=conn.get('host'),username=conn.get('user'),password=conn.get('pwd'),
                database=conn.get('src_url'),port=conn.get('port'),charset=conn.get('charset')
            )
            data = dbConnection.selectDB(conn.get('fetch_method'))
            temp_info['data'] = data
        elif conn.get('type') == "impala数据源":
            pass
        tableInfo.append(temp_info)
    return tableInfo

def configRead(request):
    db_conn_info = getConfigInfo()
    return HttpResponse(json.dumps(db_conn_info),content_type="application/json")

def tableInfo(request):
    sql = '''SELECT dcd.id,dcd.fetch_method,dcd.table_name,dcd.remark AS rm1, 
                 dcs.type, dcs.src_url, dcs.host, dcs.port, dcs.user, dcs.pwd, dcs.charset
                 FROM dictionary_configdata AS dcd 
                 LEFT JOIN dictionary_configsrc AS dcs 
                 ON dcd.name_id = dcs.id;'''
    db_conn_info = getConfigInfo(sql)

    table_info = getTableInfo(db_conn_info)
    return HttpResponse(json.dumps(table_info,cls=DjangoJSONEncoder), content_type="application/json")

def product(request):
    # 获取数据库关联表信息
    sql = '''SELECT dsp.id,dsp.table,dsp.title, 
                 dcs.type, dcs.src_url, dcs.host, dcs.port, dcs.user, dcs.pwd, dcs.charset
                 FROM dictionary_systemproduct AS dsp 
                 LEFT JOIN dictionary_configsrc AS dcs 
                 ON dsp.configsrc_id = dcs.id LIMIT 10;'''
    db_conn_info = getConfigInfo(sql)
    data_parent_tree = []
    for i in db_conn_info:
        temp_info = {}

        sql_conditon = i.get('title')
        sql_withCondi = '''SELECT id,x_axis,x_cn,y_axis,y_cn,z_axis,z_cn,unit,chart_type,time_cyc,chart_descrip,stat_way,read_field
        FROM dictionary_dataproduct WHERE title = '%s';''' % (sql_conditon)
        child_info = getConfigInfo(sql_withCondi)

        temp_info['sys_id'] = i.get('id')
        temp_info['title'] = i.get('title')
        temp_info['table'] = i.get('table')
        temp_info['type'] = i.get('type')
        # temp_info['src_url'] = i.get('src_url')
        # temp_info['host'] = i.get('host')
        # temp_info['port'] = i.get('port')
        # temp_info['user'] = i.get('user')
        # temp_info['pwd'] = i.get('pwd')
        # temp_info['charset'] = i.get('charset')

        # temp_info['children'] = child_info

        data_children_tree = []
        for j in child_info:
            temp_child_info = {}
            temp_child_info['id'] = j.get('id')
            temp_child_info['x_axis'] = j.get('x_axis')
            temp_child_info['x_cn'] = j.get('x_cn')
            temp_child_info['y_axis'] = j.get('y_axis')
            temp_child_info['y_cn'] = j.get('y_cn')
            temp_child_info['z_axis'] = j.get('z_axis')
            temp_child_info['z_cn'] = j.get('z_cn')
            temp_child_info['unit'] = j.get('unit')
            temp_child_info['chart_type'] = j.get('chart_type')
            temp_child_info['time_cyc'] = j.get('time_cyc')
            temp_child_info['chart_descrip'] = j.get('chart_descrip')
            temp_child_info['stat_way'] = j.get('stat_way')
            # temp_child_info['read_field'] = j.get('read_field')
            if i.get('type') == "mysql数据源":
                dbConnection = dbConn.mysql(
                    host=i.get('host'), username=i.get('user'), password=i.get('pwd'),
                    database=i.get('src_url'), port=i.get('port'), charset=i.get('charset')
                )
                data = dbConnection.selectDB(j.get('read_field'))
                temp_child_info['data'] = data
            data_children_tree.append(temp_child_info)

        temp_info['children'] = data_children_tree

        data_parent_tree.append(temp_info)

    return HttpResponse(json.dumps(data_parent_tree,cls=DjangoJSONEncoder), content_type="application/json")


# 递归实现列表数据转化嵌套json
def list_to_tree(treedata, parentID = 0):
    temp = []
    treelist = treedata

    for index, item in enumerate(treelist):

        if (item.get('parentID') == parentID):

            if len(list_to_tree(treelist, (treelist[index].get('id')))) > 0:

                treelist[index]['children'] = list_to_tree(treelist, treelist[index].get('id'))

            temp.append(treelist[index])

    return temp


def treemenu(request):
    sql = '''SELECT * FROM dictionary_configmenu;'''
    db_conn_info = getConfigInfo(sql)
    treedata = list_to_tree(db_conn_info)
    return HttpResponse(json.dumps(treedata), content_type="application/json")