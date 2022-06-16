
import flask
import sqlite3
import pandas
import matplotlib.pyplot as plt


app = flask.Flask(__name__)

def query_db(query, args=(), one=False):
    db = sqlite3.connect('data.db')
    cur = db.cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return (r[0] if r else None) if one else r

@app.route('/')
def show():
    page = "<body> <ol>"
    data = query_db("select * from winners")
    for value in data:
        page += '<li>{year} {age} {awardee} {gender} {movie}</li>'.format(**value)
    page += "</ol></body>"
    return page


app.run()
