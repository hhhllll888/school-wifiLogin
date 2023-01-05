import requests
from urllib import parse
import json

def main(you_user: str, you_password: str):
    if you_password == '' and you_user == '':
        print('没有账号密码')
    global back  # 请求获取设备当前wlanid和userid地址
    jumpurl = "http://10.202.1.23/eportal/redirectortosuccess.jsp"  # 请求设备获取当前wlanid和userid地址
    sendurl = "http://10.202.1.23/eportal/InterFace.do?method=login"  # 登陆地址
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/83.17763'}
    try:
        r = requests.get(jumpurl, headers=head)
    except:
        print('可能你不在校园网环境下，输入10.202.1.23查看是否跳转到登陆页面')
        print('如果还是没有可能是登陆页面做了调整，联系开发者重新适配')
        return
    back = r.content.decode('utf-8')  # 这里注意下，如果返回的是http://www.chzc.edu.cn就是登陆成功了
    if "http://www.chzc.edu.cn" in back:
        return print('你已经登陆成功，无需再次登陆')
    urlR = back.strip().split("?")[1]
    querystring = parse.quote(urlR)
    data = {
        "userId": you_user,  # 你的用户名
        "password": you_password,  # 你的密码
        "service": "",
        "operatorPwd": "",
        "operatorUserId": "",
        "validcode": "",
        "passwordEncrypt": "false",
        "queryString": querystring
    }
    data2 = {"method": "login"}
    cookie = {
        "EPORTAL_COOKIE_USERNAME": you_user,
        "EPORTAL_COOKIE_PASSWORD": you_password,
        "EPORTAL_COOKIE_SERVER": "",
        "EPORTAL_COOKIE_SERVER_NAME": "",
        "EPORTAL_COOKIE_OPERATORPWD": "",
        "EPORTAL_COOKIE_DOMAIN": "",
        "EPORTAL_COOKIE_SAVEPASSWORD": "true",
        "EPORTAL_AUTO_LAND": "",
    }
    # 不加      "JSESSIONID"试试
    r = requests.post(sendurl, data=data, params=data2, headers=head, cookies=cookie)
    back = r.content.decode('utf-8')
    print(back) # 返回success登陆成功


if __name__ == "__main__":
    main('', '')  # 你学校的账号密码
