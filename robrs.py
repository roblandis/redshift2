import psycopg2
import numpy as np
import pandas as pd
from sqlalchemy import create_engine


    


#REDSHIFT CONNECTION
conn=psycopg2.connect(dbname='testdb', host='rob-apto-test.cxccv3quijkn.us-west-1.redshift.amazonaws.com', port='5439',user='admin',password='Apt0Admin')
#CURSOR
cur=conn.cursor()
#SQL SCRIPT
cur.execute("select version();")
sqlscript=cur.fetchall()
print(sqlscript)


csvfile="../filestodb/Uploaded_files/Orders.csv"
tablename="Orders"

try:
    df=pd.read_csv(csvfile,sep=',')
except:
    df=pd.read_csv(csvfile,encoding ="iso-8859-1",sep=',')

#remove spaces in header with _ 
header = list(df.columns.values)
nospaceheader = []
for head in header:
    newhead=head.replace(' ','_')
    nospaceheader.append(newhead)
df.columns=nospaceheader
#adds df to database

df.to_sql(tablename, conn, index=False, if_exists='replace')

print(df[0:2])   







#CLOSE!!!
cur.close()
conn.close()