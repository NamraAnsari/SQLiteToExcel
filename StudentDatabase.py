import sqlite3


class StudentData:

    @staticmethod
    def create_tables():
        conn = sqlite3.connect('record.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE STUDENT(S_ID INTEGER PRIMARY KEY AUTOINCREMENT, S_NAME VARCHAR(50) NOT NULL,"
                       " S_POSITION VARCHAR(50) NOT NULL)")


StudentData.create_tables()