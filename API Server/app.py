from flask import Flask
import psycopg2
from flask import request, jsonify
from psycopg2.extras import RealDictCursor
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(
   database="d7m1sonboebnpr", 
   user='gppafqfrzgxajy', 
   password='156653557573226c1688f8ec9587f3f64f7831bbc5904c60fd65d99eaba57bd7', 
   host='ec2-34-246-227-219.eu-west-1.compute.amazonaws.com', 
   port= '5432'
)

@app.route("/")
def index():
    return "This is the API page of Smart Refrigerator SAU project made by Osman Cetin <br> To go last temperature info: /api/get_last_temperature_info <br> To go last door status info: /api/get_last_door_status_info"

@app.route('/api/get_last_temperature_info', methods=['GET'])
def api_get_last_temperature_info():
    cur = conn.cursor(cursor_factory=RealDictCursor)
    query_sql = "SELECT * FROM tbl_sr_temperature_info ORDER BY temperature_date DESC FETCH FIRST 1 ROWS ONLY" 
    cur.execute(query_sql)
    results = cur.fetchall()
    return jsonify(results)

@app.route('/api/get_last_50_temperature_info', methods=['GET'])
def api_get_last_50_temperature_info():
    cur = conn.cursor(cursor_factory=RealDictCursor)
    query_sql = "SELECT * FROM tbl_sr_temperature_info ORDER BY temperature_date DESC FETCH FIRST 50 ROWS ONLY" 
    cur.execute(query_sql)
    results = cur.fetchall()
    return jsonify(results)

@app.route('/api/get_last_door_status_info', methods=['GET'])
def api_get_last_door_status_info():
    cur = conn.cursor(cursor_factory=RealDictCursor)
    query_sql = "SELECT * FROM tbl_sr_door_status_info ORDER BY status_date DESC FETCH FIRST 1 ROWS ONLY" 
    cur.execute(query_sql)
    results = cur.fetchall()
    return jsonify(results)

@app.route('/api/get_last_20_door_status_info', methods=['GET'])
def api_get_last_20_door_status_info():
    cur = conn.cursor(cursor_factory=RealDictCursor)
    query_sql = "SELECT * FROM tbl_sr_door_status_info ORDER BY status_date DESC FETCH FIRST 20 ROWS ONLY" 
    cur.execute(query_sql)
    results = cur.fetchall()
    return jsonify(results)