import logging

logging.basicConfig(filename="demo.log",level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%Y - %m -%d %H:%M:%S")

logging.info("Application process started")
logging.warning("5 records contains missing email address")
logging.error("App is critical state")


import logging
logging.basicConfig(level=logging.ERROR)

try:
    result = 10 / 0
except Exception:
    logging.exception("An error occurred")


import logging

logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s: %(message)s")

def get_balance(balance):
    try:
        result = 10000 / balance
        logging.info("Balance Calculation is done")
        return result
    except Exception:
        logging.exception("Balance calculation failed")
        return None


print(get_balance(2))
print(get_balance(0))




'''
read emp.csv file - line by line
search - dept is sales and living City is pune
         =============                   ======
                                          |->Substitute to Hyderabad
                                                           ==========
'''
import re
fname = "C:\\Users\\karth\\emp.csv"

fobj = open(fname,'r')
for var in fobj:
    if(re.search('sales',var,re.I)):
        s = re.sub('pune','HYDERABAD',var)
        if('HYDERABAD' in s):
            print(s.strip())




'''
S = ['120GB','500GB','GB200','150Gb','300gb','400']

Calculate sum of the size - display total size
'''
import re
S = ['120GB','500GB','GB200','150Gb','300gb','400']

total = 0
for var in S:
    size = re.sub('[A-Za-z]','',var)
    total = total + int(size)

print(f' Sum of {S} disk size is:{total} GB\n')

print([re.sub('[A-Za-z]','',var) for var in S])

import threading
balance = 1000

lock = threading.Lock()
def f1_deposit():
    global balance 
    with lock:
        balance = balance + 500
        
def f2_withdraw():
    global balance
    with lock:
        balance = balance - 200
        
t1 = threading.Thread(target=f1_deposit)
t2 = threading.Thread(target=f2_withdraw)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Balance : {balance}")


import sqlite3

try:
    conn = sqlite3.connect("C:\\users\\karth\\prod.db")
except Exception as eobj:
    print("DB Connection failed."+str(eobj))

sth = conn.cursor()
sth.execute("select *from prod")
for var in sth:
    print(var)
conn.close()