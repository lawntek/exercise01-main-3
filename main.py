
import sys
import glob
import sqlite3
import string
import traceback
import csv

db = sqlite3.connect('data.db')


def get_data(pathname):
    output = []
    with open(pathname) as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['gender'] = 'female' if 'female' in pathname else 'male'
            output.append(row)
    return output


def setup_db():
    try:
        cur = db.cursor()
        cur.execute("""
            create table winners
            (year integer,
            age integer,
            awardee text,
            gender text,
            movie text)
            """)
    except:
        pass


def insert_row(row):
    try:
        cur = db.cursor()
        print('inserting row', row)
        cur.execute("""insert into winners
            (year, age, awardee, gender, movie)
            values (?, ?, ?, ?, ?)""", (
                row.get('Year'),
                row.get('Age'),
                row.get('Name'),
                row.get('gender'),
                row.get('Movie'),
                ))
            #values ({Year}, {Age}, {Name}, {gender}, ?)""".format(**row), (row.get('Movie'),))
        cur.connection.commit()
    except:
        print(traceback.format_exc())
        pass



setup_db()
for f in sys.argv:
    data = []
    if f.endswith('.csv'):
        data.extend(get_data(f))
    for row in data:
        insert_row(row)
