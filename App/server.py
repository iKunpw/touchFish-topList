from App.common import secure
from flask import jsonify
from App import db
from App.models import *
import time
import datetime
import calendar


class server():
    def serverCategoryAdd(self, cat_name, username, is_delete="1"):
        check_duplicate_cat_name = t_server_category.query.filter_by(
            cat_name=cat_name).one_or_none()
        if check_duplicate_cat_name:
            data = {
                'code': 403,
                'message': "重复的分类名称！"
            }
            return jsonify(data)
        else:
            cat_add = t_server_category()
            cat_add.cat_name = cat_name
            cat_add.is_delete = is_delete
            cat_add.create_user = username
            cat_add.create_time = calendar.timegm(time.gmtime())
            # 将新创建的用户添加到数据库会话中
            db.session.add(cat_add)
            # 将数据库会话中的变动提交到数据库中, 记住, 如果不 commit, 数据库中是没有变化的.
            db.session.commit()
            if cat_add:
                data = {
                    'code': 200,
                    'message': "分类创建成功！"
                }
            return jsonify(data)

    def serverCategoryDelete(self, del_id):
        check_cat = t_server_category.query.filter_by(id=del_id).one_or_none()
        if check_cat:
            cat_del = t_server_category.query.filter_by(id=del_id).first()
            cat_del.is_delete = 1
            db.session.commit()
            if cat_del:
                data = {
                    'code': 200,
                    'message': "删除成功！"
                }
                return jsonify(data)
            else:
                data = {
                    'code': 403,
                    'message': "删除失败！"
                }
                return jsonify(data)

    def serverCategoryList(self, page, count):
        queryList = t_server_category.query.paginate(int(page), int(count),False)
        queryTotal = t_server_category.query.count()
        results = []
        for i in queryList.items:
            results.append(i.to_json())
        data = {
            'code': 200,
            'current_page': page,
            'count': count,
            'total': queryTotal,
            'data': results
        }
        return jsonify(data)
