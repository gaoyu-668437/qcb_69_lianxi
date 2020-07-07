
#获取所有数据
from http_homeWork.data_infomation import read_information
#获取http请求
from http_homeWork.http_request import http_request

from http_homeWork.data_infomation import write_data

import json

#全局变量
Token = None

def run(file_name,sheet_name,c1,c2):
    null = None
    all_information = read_information(file_name,sheet_name)
    print(all_information)
    # header_1 = {'X-Lemonban-Media-Type': 'lemonban.v2'}
    uri = 'http://120.78.128.25:8766'
    # result_login = http_request(uri+all_information[0][4],eval(all_information[0][5]))
    # token = result_login['data']['token_info']['token']
    for i in range(len(all_information)):
        global Token
        if 'GET' in all_information[i][3]:
            result = http_request(uri + all_information[i][4], token=Token,
                                  method=all_information[i][3])
        else:
            result = http_request(uri + all_information[i][4], eval(all_information[i][5]),token=Token,method=all_information[i][3])
            if sheet_name == 'login':
                Token = None
            elif 'login' in all_information[i][4]:
                Token = 'Bearer ' + result['data']['token_info']['token']
        print('第{}条{}用例执行的结果为：{}'.format(all_information[i][0],all_information[i][2],result))
        # else:
        #     method = all_information[i][3]
        #     url = uri+all_information[i][4]
        #     information_data = eval(all_information[i][5])
        #     hope_information = eval(all_information[i][6])
        #     # print(url,information_data,hope_information,method)
        #     print('第{}条充值测试用例充值的结果为：{}'.format(all_information[i][0],http_request(url,information_data,Token)))
        # #将获取到的结果写入Excel中
        #         # wb = load_workbook(file_name)
        #         # wb[sheet].cell(row = all_information[i][0]+1,column = 8).value = str(result)
        #         # real = {'code':result['code'],'msg':result['msg']}
        #         # if eval(all_information[i][6]) == real:
        #         #     wb[sheet].cell(row = all_information[i][0]+1,column = 9).value = 'PASS'
        #         # else:
        #         #     wb[sheet].cell(row=all_information[i][0] + 1, column=9).value = 'FAIE'
        #         # wb.save(file_name)
        write_data(file_name,sheet_name,all_information[i][0]+1,c1,str(result))
        real = {'code': result['code'], 'msg': result['msg']}
        if eval(all_information[i][6]) == real:
            write_data(file_name, sheet_name, all_information[i][0] + 1, c2, 'PASS')
        else:
            write_data(file_name, sheet_name, all_information[i][0] + 1, c2, 'FAIL')




#执行充值操作
run('data_information.xlsx','recharge',8,9)
#执行注册操作
run('data_information.xlsx','register',8,9)
#执行登录操作
run('data_information.xlsx','login',8,9)
#执行取现操作
run('data_information.xlsx','withdraw',8,9)
#执行更改昵称操作
run('data_information.xlsx','name_update',8,9)
#执行获取用户信息操作
run('data_information.xlsx','user_info',8,9)





