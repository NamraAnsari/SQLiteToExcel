import sqlite3
import csv
import os


class ManageStudentEntry:

    def __init__(self):
        self.conn = sqlite3.connect('record.db')
        self.cursor = self.conn.cursor()

    def insert_entry(self, name, pos):
        self.cursor.execute("INSERT INTO STUDENT (S_NAME, S_POSITION) VALUES(?,?)", (name, pos))
        self.conn.commit()

    def view_entry(self):
        self.cursor.execute("SELECT * FROM STUDENT")
        result = self.cursor.fetchall()
        print(result)
        path_of_file = 'C:\\Users\\Namra Ansari\Documents\data.xls'
        # cwd = os.getcwd()
        # files = os.listdir(cwd)
        # print("Files in '%s': %s" % (cwd, files))
        with open(path_of_file, 'w') as xls_file:
            csv_writer = csv.writer(xls_file, delimiter='\t')
            csv_writer.writerow(['ID', 'Name', 'Position'])
            for row in result:
                csv_writer.writerow(row)

    def __exit__(self):
        self.conn.close()