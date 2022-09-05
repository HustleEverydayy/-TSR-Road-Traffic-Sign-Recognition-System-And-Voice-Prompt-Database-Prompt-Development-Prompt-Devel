# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 21:55:18 2022

@author: CFuser
"""

import pymysql
dbhost='Localhost'
dbuser='root'
dbpass=''
dbname='camera'
charset='utf8'
db=pymysql.connect(host=dbhost,user=dbuser,password=dbpass,database=dbname,charset=charset)
#a='120.89102'
#b=' '24.67400
a=input('經度:')
b=input('緯度:')
a1=str(float(a)+0.0005)
a2=str(float(a)-0.0005)
b1=str(float(b)+0.0005)
b2=str(float(b)-9.0005)
#SQL 語法
#sq1 = "SELECT * FROM c"
#sq1 ="SELECT * FROM c WHERE limit "
try:
    cursor = db.cursor()
    # 執行SQL语句
    sql = "SELECT * FROM c"
    #sq1 ="SELECT * FROM c WHERE cityName=%s "
    #sql ="SELECT * FROM c WHERE RegionName=%s "
    cursor.execute(sql)
    #cursor.execute(sq1,(''))
    #使用fetchall()得到所有資料
    results = cursor.fetchall()
    for row in results:
        CityName=row[0]
        RegionName=row[1]
        Address=row[2]
        DeptNm=row[3]
        BranchNm=row[4]
        Longitude=row[5]
        Latitude=row[6]
        direct=row[7]
        limit=row[8]
        #print (row)
        if a2 <= row[5] <= a1 :
            if b2 <= row[6] <= b1:
                print ("Limit:"+row[8])
except:
    print ("Error: unable to fetch data")