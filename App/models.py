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

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

class t_v2ex_hot(db.Model):
    __tablename__='t_v2ex_hot'
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.Text())
    url=db.Column(db.Text())
    update_time=db.Column(db.Text())

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

class t_weibo_hot(db.Model):
    __tablename__='t_weibo_hot'
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.Text())
    url=db.Column(db.Text())
    update_time=db.Column(db.Text())

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

class t_52pojie_hot(db.Model):
    __tablename__='t_52pojie_hot'
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.Text())
    url=db.Column(db.Text())
    update_time=db.Column(db.Text())

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict
        