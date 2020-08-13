from lxml import etree
from flask import jsonify
from urllib import parse
from App import db
from App.models import *

class get_hot:
        def get_zhihu(self):
            queryList = t_zhihu_hot.query.all()
            queryTotal = t_zhihu_hot.query.count()
            results = []
            for i in queryList:
                results.append(i.to_json())
            data = {
                'code': 200,
                'data': results
            }
            db.session.close()
            return jsonify(data)

        def get_v2ex(self):
            queryList = t_v2ex_hot.query.all()
            queryTotal = t_v2ex_hot.query.count()
            results = []
            for i in queryList:
                results.append(i.to_json())
            data = {
                'code': 200,
                'data': results
            }
            db.session.close()
            return jsonify(data)
        
        def get_weibo(self):
            queryList = t_weibo_hot.query.all()
            queryTotal = t_weibo_hot.query.count()
            results = []
            for i in queryList:
                results.append(i.to_json())
            data = {
                'code': 200,
                'data': results
            }
            db.session.close()
            return jsonify(data)

        def get_52pojie(self):
            queryList = t_52pojie_hot.query.all()
            queryTotal = t_52pojie_hot.query.count()
            results = []
            for i in queryList:
                results.append(i.to_json())
            data = {
                'code': 200,
                'data': results
            }
            db.session.close()
            return jsonify(data)