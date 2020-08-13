from App import db
from sqlalchemy import func
from sqlalchemy import Integer, String, Enum, Column
from sqlalchemy.ext.declarative import declarative_base

class t_zhihu_hot(db.Model):
    __tablename__ = 't_zhihu_hot'
    id = db.Column(db.INTEGER, primary_key=True)
    title=db.Column(db.Text())
    # content=db.Column(db.Text())
    url=db.Column(db.Text())
    update_time = db.Column(db.INTEGER, nullable=False)

# class t_v2ex_hot(db.Model):
#     __tablename__='t_v2ex_hot'
#     id = db.Column(db.Integer, primary_key=True)
#     title=db.Column(db.Text())
#     url=db.Column(db.Text())
#     update_time=db.Column(db.Text())
