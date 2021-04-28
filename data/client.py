import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class Client(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'client'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    patronymic = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    passport = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    usluga = sqlalchemy.Column(sqlalchemy.String, nullable=True)
