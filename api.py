import flask
from flask import request, jsonify
import sqlite3
import numpy as np 

# Debug allows for changes to be seen in real time.
app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dictFactory(cursor, row):
    """
    Function that parses the entries of the database and returns them as a list of dictionaries.

    @param cursor -- A cursor object using sqlite.
    @param row -- The row of the database being parsed.
    """
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def homePage():
    return '''
    <h1>Data PNS dan Jabatannya di Jawa Barat</h1>
    <h3>You have reached: /home/</h3>
    <p>To view all entries in the database: '127.0.0.1:5000/api/v1/pns/getAll' </p>
    <p>To filter entries based on custom, example : '127.0.0.1:5000/api/v1/pns/getByFilter?id=1' </p>
'''

@app.route('/api/v1/pns/getAll', methods=['GET'])
def apiViewAll():
    conn = sqlite3.connect('data/data_pns.db')
    conn.row_factory = dictFactory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM tblJobs;').fetchall()

    return jsonify(all_books)

@app.errorhandler(404)
def pageNotFound(e):
    return "<h1>Error 404</h1><p>Page not found.</p>", 404

@app.route('/api/v1/pns/getByFilter', methods=['GET'])
def apiViewByFilter():
    '''
    Function that allows users to filter the results in the API based on specified input.
    '''
    query_parameters = request.args

    id = query_parameters.get('id')
    jabatan = query_parameters.get('jabatan')
    jumlah_pns = query_parameters.get('jumlah_pns')
    kode_provinsi = query_parameters.get('kode_provinsi')
    nama_provinsi = query_parameters.get('nama_provinsi')
    satuan = query_parameters.get('satuan')
    tahun = query_parameters.get('tahun')

    query = "SELECT * FROM tblJobs WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)

    if jabatan:
        query += ' jabatan=? AND'
        to_filter.append(jabatan)

    if jumlah_pns:
        query += ' jumlah_pns=? AND'
        to_filter.append(jumlah_pns)
    
    if kode_provinsi:
        query += ' kode_provinsi=? AND'
        to_filter.append(kode_provinsi)

    if nama_provinsi:
        query += ' nama_provinsi=? AND'
        to_filter.append(nama_provinsi)

    if satuan:
        query += ' satuan=? AND'
        to_filter.append(satuan)

    if tahun:
        query += ' tahun=? AND'
        to_filter.append(tahun)


    if not (id or jabatan or jumlah_pns or kode_provinsi or nama_provinsi or satuan or tahun):
        return pageNotFound(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('data/data_pns.db')
    conn.row_factory = dictFactory
    cur = conn.cursor()
    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)


    

app.run()