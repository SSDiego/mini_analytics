# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 19:39:52 2022

@author: sp2di
"""

import os

os.chdir(r"D:\projectLN\sqlite")




import sqlite3

#1

conn = sqlite3.connect('test_database') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS products
          ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT)
          ''')
          
c.execute('''
          CREATE TABLE IF NOT EXISTS prices
          ([product_id] INTEGER PRIMARY KEY, [price] INTEGER)
          ''')
                     
conn.commit()


#2

conn = sqlite3.connect('test_database') 
c = conn.cursor()
                   
c.execute('''
          INSERT INTO products (product_id, product_name)

                VALUES
                (1,'Computer'),
                (2,'Printer'),
                (3,'Tablet'),
                (4,'Desk'),
                (5,'Chair')
          ''')

c.execute('''
          INSERT INTO prices (product_id, price)

                VALUES
                (1,800),
                (2,200),
                (3,300),
                (4,450),
                (5,150)
          ''')

conn.commit()


#3

import pandas as pd

conn = sqlite3.connect('test_database') 
c = conn.cursor()
                   
c.execute('''
          SELECT
          a.product_name,
          b.price
          FROM products a
          LEFT JOIN prices b ON a.product_id = b.product_id
          ''')

df = pd.DataFrame(c.fetchall(), columns=['product_name','price'])
print (df)


#4

conn = sqlite3.connect('test_database2')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS products (product_name text, price number)')
conn.commit()

data = {'product_name': ['Computer','Tablet','Monitor','Printer'],
        'price': [900,300,450,150]
        }

df = pd.DataFrame(data, columns= ['product_name','price'])

df.to_sql('products', conn, if_exists='replace', index = False)
 
c.execute('''  
SELECT * FROM products
          ''')

for row in c.fetchall():
    print (row)
    
    
#5 
conn = sqlite3.connect('test_database3') 
c = conn.cursor()    

c.execute('CREATE TABLE IF NOT EXISTS products (product_name text, price number)')
conn.commit()

data = {'product_name': ['Computer','Tablet','Monitor','Printer'],
        'price': [900,300,450,150]
        }

df = pd.DataFrame(data, columns= ['product_name','price'])

c.execute('''  
		SELECT * FROM products
		WHERE price = (SELECT max(price) FROM products)
          ''')
        
df = pd.DataFrame(c.fetchall(), columns=['product_name','price'])    
print (df)



conn = sqlite3.connect('test_database3') 
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS products (product_name text, price number)')
conn.commit()

data = {'product_name': ['Computer','Tablet','Monitor','Printer'],
        'price': [900,300,450,150]
        }

df = pd.DataFrame(data, columns= ['product_name','price'])
df.to_sql('products', conn, if_exists='replace', index = False)

c.execute('''  
		SELECT * FROM products
		WHERE price = (SELECT max(price) FROM products)
          ''')

df = pd.DataFrame(c.fetchall(), columns=['product_name','price'])    
print (df)
