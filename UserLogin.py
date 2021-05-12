# -*- coding: utf-8 -*-
"""
Created on Mon May  3 23:01:25 2021

@author: sneha
"""
import mysql.connector
import Stock_Reco as reco
from getpass import getpass


def login():
    cnx = mysql.connector.connect(host="localhost", user="root", db="nyse") 
    cur = cnx.cursor(buffered=True)
    print("Login")
    #print(cnx.is_connected())
    email = input("email:")
    password = getpass()
    query = "select * from user_login where email= '"+email+"' and password = '"+password+"';"
    #print(query)
    cur.execute(query)
    user_id = cur.fetchone()[0]
    #print(user_id)
    profile= "select * from user_profile where user_id='"+str(user_id)+"';"
    cur.execute(profile)
    u_prof = cur.fetchone()
    reco.stock_list(u_prof[1], u_prof[2], u_prof[3])
    cur.close()
    cnx.close()

def sign_up():
    cnx = mysql.connector.connect(host="localhost", user="root", db="nyse") 
    cur = cnx.cursor(buffered=True)
    print("Sign up")
    first_name=""
    last_name=""
    email=""
    password=""
    risk_apt = 0
    yearly_inv = 0
    exp_return = 0
    #print("First Name:")
    first_name = input("first name:")
    last_name = input("last name:")
    email = input("email:")
    password = getpass()
    print("please answer following questions")
    print("""1. What is your age?
        a. 18 to 25
        b. 25 to 30
        c. 30 to 35
        d. 35 to 40
        e. 40 to 50
        f. 50 to 60
        g. 60+""")
    q1 = input("input:")
    if q1=='a':
        risk_apt+=70
    elif q1=='b':
        risk_apt+=60
    elif q1=='c':
        risk_apt+=50
    elif q1=='d':
        risk_apt+=40
    elif q1=='e':
        risk_apt+=30
    elif q1=='f':
        risk_apt+=20
    elif q1=='g':
        risk_apt+=10
    else:
        print("invalid input")

    print("""2. What is your profession?
        a. Student
        b. Salaried Employee
        c. Entraprenaur
        d. Business""")
    q2 = input("input:")
    if q2=='a':
        risk_apt+=20
    elif q2=='b':
        risk_apt+=40
    elif q2=='c':
        risk_apt+=60
    elif q2=='d':
        risk_apt+=70
    else:
        print("invalid input")
    print("""3. How many dependents do you have?
        a. 0
        b. 1
        c. 2
        d. 3
        e. 3+ """)
    q3 = input("input:")
    if q3=='a':
        risk_apt+=70
    elif q3=='b':
        risk_apt+=60
    elif q3=='c':
        risk_apt+=50
    elif q3=='d':
        risk_apt+=40
    elif q3=='e':
        risk_apt+=30
    else:
        print("invalid input")    
    print("""4. What is your monthly income?
        a. >200000
        b. <200000
        c. <150000
        d. <140000
        e. <45000""")
    q4 = input("input:")
    if q4=='a':
        risk_apt+=70
    elif q4=='b':
        risk_apt+=60
    elif q4=='c':
        risk_apt+=50
    elif q4=='d':
        risk_apt+=40
    elif q4=='e':
        risk_apt+=30
    else:
        print("invalid input")
    print("5. How much money you are willing to invest every year?")
    yearly_inv= input("input:")          

    print("6. How much is your percetage expected return? (enter a number from 1 to 100)")
    temp = int(input("input:"))
    if (temp >=0 and temp <=100):
        exp_return = temp/100
    else:
        print("invalid Input")    
    risk_apt = (risk_apt/400)
    
    insert_login = "insert into user_login (first_name, last_name, email, password) values ('"+first_name+"','"+last_name+"','"+email+"','"+password+"');"
    
    cur.execute(insert_login)
    query_mid = "select user_id from user_login where email= '"+email+"' and password = '"+password+"';"
    #print(query_mid)
    cur.execute(query_mid)
    user_id = cur.fetchone()[0]
    insert_profile = "insert into user_profile (user_id, risk_apt, yearly_inv, exp_return) values ("+str(user_id)+","+str(risk_apt)+","+str(yearly_inv)+","+str(exp_return)+");"
    cur.execute(insert_profile)
    cnx.commit()
    print("You are all set!")
    cur.close()
    cnx.close()
    login()
