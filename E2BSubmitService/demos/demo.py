import pymysql
import os
from xml.dom import minidom
import json
from flask import Blueprint, render_template, redirect, Flask,current_app
demo = Blueprint('demo', __name__)


@demo.route('/getdata')
def index():
    conn = pymysql.connect(host='127.0.0.1', user='system', password='Nnio2018', database='pve2b', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = 'SELECT username,email,password FROM pve2b.user;'
    cursor.execute(sql)
    data = json.dumps(cursor.fetchall())
    cursor.close()
    conn.close()
    return data;


@demo.route('/demo/getdata/')
def getdata():
    conn = pymysql.connect(host='127.0.0.1', user='system', password='Nnio2018', database='pve2b', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = 'SELECT username,email,password FROM pve2b.user;'
    cursor.execute(sql)
    data = json.dumps(cursor.fetchall())
    cursor.close()
    conn.close()
    return data;


@demo.route('/processICSR')
def modify_icsr():
    xml_path = current_app.config['XMLPATH']
    with open(xml_path + 'E2B_R3.xml', 'r+', encoding='utf8') as fh:
        dom = minidom.parse(fh)
        root = dom.documentElement

        print(root.nodeName)
        print(root.childNodes)
    return '';