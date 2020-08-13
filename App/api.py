from flask import Flask, request, jsonify, make_response
from App import create_app
from App.refreshHot import refresh_hot
from App.getHot import get_hot

app = create_app()

@app.after_request
def af_request(resp):
    """
    #请求钩子，在所有的请求发生后执行，加入headers。
    :param resp:
    :return:
    """
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = 'content-type,token,username,expire_time'
    resp.headers['Access-Control-Expose-Headers'] = 'token, username, expire_time'
    return resp


@app.route('/')
def ikunsounds():
    return 'Welcome!'


# @app.route('/api/', methods=['POST'])
# def register():
#     if request.method == "POST":
#         username = request.json.get('username')
#         password = request.json.get('password')
#         data = {
#             'data': user().reg(username, password)
#         }
#         return jsonify(data)

@app.route('/api/refresh', methods=['POST'])
def refresh():
    if request.method == "POST":
        return refresh_hot().refresh()


@app.route('/api/refresh_zhihu', methods=['POST'])
def refresh_zhihu():
    if request.method == "POST":
        data = refresh_hot().refresh_zhihu()        
        return data

@app.route('/api/refresh_v2ex', methods=['POST'])
def refresh_v2ex():
    if request.method == "POST":
        data = refresh_hot().refresh_v2ex()        
        return data

@app.route('/api/refresh_weibo', methods=['POST'])
def refresh_weibo():
    if request.method == "POST":
        data = refresh_hot().refresh_weibo()        
        return data

@app.route('/api/refresh_52pojie', methods=['POST'])
def refresh_52pojie():
    if request.method == "POST":
        data = refresh_hot().refresh_52pojie()        
        return data

@app.route('/api/get_zhihu', methods=['POST'])
def getZhihu():
    if request.method == "POST":
        data = get_hot().get_zhihu()
        return data

@app.route('/api/get_v2ex', methods=['POST'])
def getv2ex():
    if request.method == "POST":
        data = get_hot().get_v2ex()
        return data

@app.route('/api/get_52pojie', methods=['POST'])
def get52pojie():
    if request.method == "POST":
        data = get_hot().get_52pojie()
        return data

@app.route('/api/get_weibo', methods=['POST'])
def getWeibo():
    if request.method == "POST":
        data = get_hot().get_weibo()
        return data

