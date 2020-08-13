from App.models import *
from flask import jsonify

class secure():
    def hashlib_md5(self, string):
        import hashlib
        # 初始化hashlib
        m = hashlib.md5()
        # hashlib只能操作bytes的数据，所以此处将str转换为bytes，UTF-8
        b = string.encode(encoding='utf-8')
        m.update(b)
        str_md5 = m.hexdigest()
        return str_md5

    def create_token_str(self, username):
        import random
        import time
        import string
        random_str = ''.join(random.sample(
            string.ascii_letters + string.digits, 8))
        time = time.time()
        token = secure().hashlib_md5(str(random_str) + str(time) + str(username))
        return token

    def auth(self, token):
         tokenAuth = t_sys_token.query.filter_by(token=token).one_or_none()
         if tokenAuth == None:
            data = {
                'code': 401,
                'message': "非法请求！"
            }
            return jsonify(data)