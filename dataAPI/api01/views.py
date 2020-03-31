from django.shortcuts import HttpResponse
from django.views.decorators.http import require_http_methods
import json

from api01.impalaConn import impala

def params_conv_sql(json_result):
    sql_main = 'SELECT * from '
    sql_cond = ''
    count = 0
    for param in json_result:
        if param == "api_name":
            sql_main = sql_main + json_result.get(param)
        else:
            if count == 1 and json_result.get(param) != '' and param.split('|')[1] == 'eq':
                sql_cond = sql_cond + param.split('|')[0] + '=' + '"' + json_result.get(param) + '"'
            elif count == 1 and json_result.get(param) != '' and param.split('|')[1] == 'gt':
                sql_cond = sql_cond + param.split('|')[0] + '>' + '"' + json_result.get(param) + '"'
            elif count == 1 and json_result.get(param) != '' and param.split('|')[1] == 'lt':
                sql_cond = sql_cond + param.split('|')[0] + '<' + '"' + json_result.get(param) + '"'
            elif count > 1 and count <= len(json_result) and json_result.get(param) != '' and param.split('|')[1] == 'eq':
                sql_cond = sql_cond + ' AND ' + param.split('|')[0] + '=' + '"' + json_result.get(param) + '"'
            elif count > 1 and count <= len(json_result) and json_result.get(param) != '' and param.split('|')[1] == 'gt':
                sql_cond = sql_cond + ' AND ' + param.split('|')[0] + '>' + '"' + json_result.get(param) + '"'
            elif count > 1 and count <= len(json_result) and json_result.get(param) != '' and param.split('|')[1] == 'lt':
                sql_cond = sql_cond + ' AND ' + param.split('|')[0] + '<' + '"' + json_result.get(param) + '"'
        count += 1
    return sql_main,sql_cond

def sqlget(sql_main,sql_cond):
    if sql_cond == '':
        return sql_main
    else:
        return sql_main + ' WHERE ' + sql_cond

# Create your views here.
@require_http_methods(["GET","POST"])
def dataget(request):
    impala_cur = impala('118.31.173.39', 25001)
    json_result = {}
    json_response_records = {}

    if (request.method == 'POST'):
        print("the POST method")
        postBody = request.body
        json_result = json.loads(postBody)
        print(json_result)

    print(params_conv_sql(json_result))
    # convert params to sql sentence
    sql_main, sql_cond = params_conv_sql(json_result)
    # get the whole sentence of sql
    sql = sqlget(sql_main, sql_cond)
    # execute the sql and output the result with df form
    df = impala_cur.exec_sql_output_df(sql)

    try:
        json_response_records = df.to_json(orient='records')
    except:
        # 针对GET请求的无效参数数据提交
        json_response_records = json.dumps({"error_msg":"no json data read"})
    finally:
        return HttpResponse(json_response_records,content_type="application/json")