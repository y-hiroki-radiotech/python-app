from sqlalchemy import Column, String, UniqueConstraint
from sqlalchemy.orm.session import Session

from app.models.db import BaseDatabase, database


class User(BaseDatabase):
    __tablename__ = "user"
    name = Column(String)
    UniqueConstraint(name)

    @staticmethod
    def get_or_create(name: str) -> Session:
        "クラスのインスタンスを作成せずにメソッドを呼び出すことができる"
        # ToDO
        session = database.connect_db()
        row = session.query(User).filter(User.name == name).first()
        if row:
            session.close()
            return row

        user = User(name=name)
        session.add(user)
        session.commit()

        # もう一度sqlからデータを持ってこないと、idが取得できない
        row = session.query(User).filter(User.name == name).first()
        session.close()
        return row
