from markupsafe import Markup
from xiaopy import *
import requests
import re
from flask import Flask, request, jsonify, render_template, make_response
import json
import time
import subprocess
api = Flask(__name__, static_url_path='', static_folder='', template_folder='')

api.config['JSON_AS_ASCII'] = False
@api.route('/api/getAndLoopAccess', methods=['POST'])
def get_and_loop_access():
    try:
        data = request.get_json()

        username = data['username']
        pass_ = data['pass']
        ServerID = data['ServerID']
        print(username,pass_,ServerID)
        cookie = 获取cookie(username, pass_, ServerID)
        print(cookie)
        if cookie == "用户名或密码错误":
            return jsonify(message='您输入的用户名或者密码错误'), 200
        matches = 获取匹配项(cookie)

        if not matches:
            return jsonify(message='未找到匹配项'), 200

        results = 获取并循环访问(cookie, matches)
        return jsonify(message='API请求成功', results=results), 200
    except Exception as error:
        print('API错误：', error)
        return jsonify(error='内部服务器错误'), 500

def 获取cookie(username, pass_, ServerID):
    session = requests.Session()
    data = {'username': username, 'pass': pass_, 'ServerID': ServerID}
    res = session.post('http://43.240.72.61:81/game_user/user/ajax.php?get=login', data=data)
    print(res.json()['code'])
    if res.json()['code'] == 1:
        return res.headers['set-cookie']
    else:
        return "用户名或密码错误"

def 获取匹配项(cookie):
    session = requests.Session()
    listRes = session.get('http://43.240.72.61:81/game_user/user/list.php', headers={'cookie': cookie})
    matches = []
    htmlCode = listRes.text
    match_pattern = r'is_yxremove\("(\d+)","(\d+)"\)'
    matches = re.findall(match_pattern, htmlCode)
    return matches

def 获取并循环访问(cookie, matches):
    session = requests.Session()
    fsckUrl = 'http://43.240.72.61:81/game_user/user/ajax.php?get=fsck'
    headers = {'Cookie': cookie}
    interval = 0.1  # 间隔时间，单位：秒
    results = []
    for match in matches:
        firstNumber, secondNumber = match
        try:
            fsckRes = session.post(fsckUrl, data={'id': firstNumber, 'game_id': secondNumber}, headers=headers)
            results.append(fsckRes.text)
            time.sleep(interval)
        except Exception as error:
            print(error)
            results.append("Error fetching fsck: " + str(error))
    return results



@api.route('/s',methods=['get','post'])
def s():
    html = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>My Flask Page</title>
        </head>
        <body>
            <h1>Hello, Flask!</h1>
            <p>This is a simple Flask web page with embedded HTML code.</p>
        </body>
        </html>
        '''
    return html


@api.route('/cx', methods=["get", "post"])
def cx():
    kk = requests.get("https://tools.mgtv100.com/external/v1/logistics/query?no=75720482780245")
    kk.encoding = 'utf-8'
    json_str = kk.text  # 获取JSON字符串


    try:
        data = json.loads(json_str)  # 解析JSON字符串为Python字典

        # 提取所需信息并格式化输出
        number = data["data"]["number"]
        list_data = data["data"]["list"]
        formatted_output = []

        for item in reversed(list_data):  # 反向遍历列表
            time = item["time"]
            status = item["status"]
            formatted_output.append(f"<div>单号: {number}</div><div>时间: {time}</div><div>状态: {status}</div>")

        # 将所有结果合并为一个字符串并返回，使用CSS来设置换行
        result = "\n".join(formatted_output)

        # 在HTML中使用CSS设置换行
        html_output = f'<div style="white-space: pre-line;">{result}</div>'

        return html_output
    except json.JSONDecodeError as e:
        return f"JSON解析错误: {str(e)}"


@api.route('/zx', methods=["get", "post"])

def zx():

    cmd = "ipconfig"
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, encoding="utf-8")
    res = p.stdout.readlines()
    xp.log(res)
    return ("nihaoya1")
@api.route('/', methods=["get", "post"])

def index():
    return render_template('index.html')



if __name__ == '__main__':
    api.run(host='0.0.0.0', port=5702, debug=False)

    print('服务器启动成功')

# api = flask.Flask(__name__)
i = 0
# 参数1-5为取图正常参数,参数6为1是点击为0是不点击，参数7为点击延时
战斗 = ["战斗.png", 1199, 170, 1275, 401, 0.9, 1, 1]
第一回合 = ["第一回合.png", 607, 5, 666, 57, 0.9, 0, 0]
取消 = ["取消.png", 1230, 636, 1258, 670, 0.9, 1, 0]
自动 = ["自动.png", 1187, 615, 1271, 700, 0.9, 1, 0]
# 所有需要找的图集合
集合 = [战斗, 第一回合, 取消, 自动]


# 封装成找图函数
def zt(x):
    t1 = xp.findImage(x[0], x[1], x[2], x[3], x[4], x[5])

    if t1:
        print(x[0])
        if x[0] == '第一回合.png':
            time.sleep(1)

            return ('z')
        else:
            if x[6] == 1:
                time.sleep(int(x[7]))
                xp.tap(t1.x, t1.y)

    else:
        return "空"
