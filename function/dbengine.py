#!/usr/bin/env python
# coding:utf-8
# manning  2015-3-29

import os
import time
import sqlite3
import gevent
import hashlib
import Queue

def set_db_folder(name):
    db_dir = os.getcwd() + '/database/'
    db_name = time.strftime("%Y-%m-%d", time.localtime())  #  2015-01-20
    folder = db_dir + str(db_name) + '-' + name[0]
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

def init_db(name,model):
    folder = set_db_folder(name)
    if model == 0:
        try:
            conn = sqlite3.connect(folder+'/complete.db')
            sql_creat_table = '''
                        create table if not exists info(
                        id integer primary key autoincrement, 
                        http_url varchar(256) DEFAULT NULL,
                        time varchar(50) DEFAULT NULL,
                        backup_1 varchar(30) DEFAULT NULL,
                        backup_2 varchar(30) DEFAULT NULL,
                        backup_3 varchar(30) DEFAULT NULL,
                        backup_4 varchar(30) DEFAULT NULL
                        )'''
            conn.execute(sql_creat_table)
            conn.close()
            return [str(folder+'/complete.db'),'']
        except Exception, e:
            print '---'+str(e)+'--'
    elif model == 1:
        try:
            conn = sqlite3.connect(folder+'/smart.db')
            sql_creat_table = '''
                        create table if not exists info(
                        id integer primary key autoincrement, 
                        http_url varchar(256) DEFAULT NULL,
                        time varchar(50) DEFAULT NULL,
                        backup_1 varchar(30) DEFAULT NULL,
                        backup_2 varchar(30) DEFAULT NULL,
                        backup_3 varchar(30) DEFAULT NULL,
                        backup_4 varchar(30) DEFAULT NULL
                        )'''
            conn.execute(sql_creat_table)
            conn.close()
            return ['',str(folder+'/smart.db')]
        except Exception, e:
            print '---'+str(e)+'--'
    elif model == 2:
        try:
            conn = sqlite3.connect(folder+'/complete.db')
            sql_creat_table = '''
                        create table if not exists info(
                        id integer primary key autoincrement, 
                        http_url varchar(256) DEFAULT NULL,
                        time varchar(50) DEFAULT NULL,
                        backup_1 varchar(30) DEFAULT NULL
                        )'''
            conn.execute(sql_creat_table)
            conn.close()
        except Exception, e:
            print '---'+str(e)+'--'
        time.sleep(1)
        try:
            conn = sqlite3.connect(folder+'/smart.db')
            sql_creat_table = '''
                        create table if not exists info(
                        id integer primary key autoincrement, 
                        http_url varchar(256) DEFAULT NULL,
                        time varchar(50) DEFAULT NULL,
                        backup_1 varchar(30) DEFAULT NULL
                        )'''
            conn.execute(sql_creat_table)
            conn.close()
            return [str(folder+'/complete.db'),str(folder+'/smart.db')]

        except Exception, e:
            print '---'+str(e)+'--'



def engine_db(dbname,complete_queue,smart_queue,model):
    connlist = init_db(dbname,model)
    #connlist[0] complete
    #connlist[1] smart
    if model == 0:#complete
        conn1 = sqlite3.connect(connlist[0])
        while True:
            try:
                if not complete_queue.empty() and not complete_queue.full():
                    t = complete_queue.get()
                    sql_insert_data = '''insert into info(http_url,time,backup_1) values ('%s', '%s', '%s')'''%(t.url,t.time,'')
                    conn1.execute(sql_insert_data)
                    conn1.commit()
            except Exception, e:
                print '---'+str(e)+'--'
                pass
    elif model == 1:#smart
        conn2 = sqlite3.connect(connlist[1])
        while True:
            try:
                if not smart_queue.empty() and not smart_queue.full():
                    t = smart_queue.get()
                    sql_insert_data = '''insert into info(http_url,time,backup_1) values ('%s', '%s', '%s')'''%(t.url,t.time,'')
                    conn2.execute(sql_insert_data)
                    conn2.commit()
            except Exception, e:
                print '---'+str(e)+'--'
                pass
    elif model == 2:#two
        conn1 = sqlite3.connect(connlist[0])
        conn2 = sqlite3.connect(connlist[1])
        while True:
            try:
                if not complete_queue.empty() and not complete_queue.full():
                    t1 = complete_queue.get()
                    sql_insert_data = '''insert into info(http_url,time,backup_1) values ('%s', '%s', '%s')'''%(t1.url,t1.time,'')
                    conn1.execute(sql_insert_data)
                    conn1.commit()
            except Exception, e:
                print '---'+str(e)+'--'
                pass
            time.sleep(0.1)
            try:
                if not smart_queue.empty() and not smart_queue.full():
                    t2 = smart_queue.get()
                    sql_insert_data = '''insert into info(http_url,time,backup_1) values ('%s', '%s', '%s')'''%(t2.url,t2.time,'')
                    conn2.execute(sql_insert_data)
                    conn2.commit()
            except Exception, e:
                print '---'+str(e)+'--'
                pass

if __name__ == "__main__": 
    init_db('levt')