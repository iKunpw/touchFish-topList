from flask import Flask, request, jsonify, make_response
from App import create_app
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

@app.route('/api/get_zhihu', methods=['POST'])
def get_zhihu():
    if request.method == "POST":
        data = get_hot().get_zhihu()        
        return data
