# MySQLdbのインポート
import MySQLdb
import os
from os.path import join, dirname
from dotenv import load_dotenv


class DataBase():
    def __init__(self):
        load_dotenv(verbose=True)
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        user = os.environ.get("USER")
        password = os.environ.get("PASSWORD")

        self.table_name = "memo"
        # データベースへの接続とカーソルの生成
        self.connection = MySQLdb.connect(
            host='localhost',
            user=user,
            passwd=password,
            db='sample',
            # テーブル内部で日本語を扱うために追加
            charset='utf8mb4'
        )
        self.cursor = self.connection.cursor()
        self.setup_table()

    def setup_table(self):
        self.cursor.execute("SHOW TABLES;")
        for table in self.cursor:
            if table[0] == self.table_name:
                return
        # テーブルの作成
        self.cursor.execute(f"""CREATE TABLE {self.table_name}(
            datetime DATETIME NOT NULL,
            text TEXT NOT NULL,
            PRIMARY KEY (datetime)
            )""")
        self.commit()

    def insert(self, text):
        # データの追加
        self.cursor.execute(
            f"""INSERT INTO {self.table_name}(datetime, text) VALUES (now(), '{text}')""")
        # 保存を実行
        self.commit()

    def select(self):
        # 一覧の表示
        self.cursor.execute(f"""SELECT * FROM {self.table_name}""")
        result = list()
        for row in self.cursor:
            result.append(row)
        self.commit()
        return result

    def commit(self):
        self.connection.commit()

    def close(self):
        # 接続を閉じる
        self.connection.close()
