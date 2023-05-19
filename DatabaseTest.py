import threading
import socket
from threading import Semaphore
import mysql.connector
db = mysql.connector.connect(user="root",password="1234",host="127.0.0.1",database="dbtest")
def connection(cursor):
    for i in range(0,1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            s.connect("google.com")
            s.close()
            cursor.execute("INSERT INTO dbtest.test(RESPONSE) VALUES(1)")
            db.commit()
        except:
            s.close()
            cursor.execute("INSERT INTO dbtest.test(RESPONSE) VALUES(0)")
            db.commit()
threadNumber = 150
threads = list()
for i in range(0,threadNumber):
    cursor = db.cursor()
    thread = threading.Thread(target=connection,args=(cursor,))
    threads.append(thread)
    thread.start()
for i in threads:
    i.join()