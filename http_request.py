
import requests  #导入




#http请求函数
def http_request(url,data=None,token= None,method = 'post'):
    header_1 = {'X-Lemonban-Media-Type': 'lemonban.v2','Authorization': token}
    if method == 'GET':
        result = requests.get(url,headers = header_1)
    elif method == 'POST':
        result = requests.post(url,json=data,headers = header_1)
    elif method == 'PATCH':
        result = requests.patch(url, json=data, headers=header_1)
    # print(result.json())
    return result.json()


if __name__ == '__main__':

    #头
    # header_1 = {'X-Lemonban-Media-Type': 'lemonban.v2'}
    #注册信息
    reg_url =  'http://120.78.128.25:8766/futureloan/member/register'
    reg_data = {"mobile_phone": "13258568252","pwd": "123456582"}
    #发起注册
    http_request(reg_url,reg_data)


    #登录信息
    log_url = 'http://120.78.128.25:8766/futureloan/member/login'
    log_data = {"mobile_phone": "13258568252","pwd": "123456582"}
    #发起登录
    response = http_request(log_url,log_data)


    #充值信息
    rec_url = 'http://120.78.128.25:8766/futureloan/member/recharge'
    rec_data = {"member_id":201444,"amount": "5000"}
    token = response['data']['token_info']['token']
    #发起充值
    http_request(rec_url,rec_data,token)


    #提现信息
    withdraw_url = 'http://120.78.128.25:8766/futureloan/member/withdraw'
    withdraw_data = {"member_id":201444,"amount": "5000"}
    #发起提现
    http_request(withdraw_url,withdraw_data,token)







# log_result = http_request(log_url,log_data,'post',headers=header_2)
# uri = 'http://120.78.128.25:8766/futureloan/member/register'


