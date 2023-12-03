#bank management system
import mysql.connector
mydb=mysql.connector.connect(host='local host',user='root',password='root',database='bms')
def open_account():
    name=input("enter your name:")
    acc=input("enter your acc number:")
    dob=input("enter your dob:")
    add=input("enter your adress:")
    ph=input("enter your contact:")
    op_bal=int(input("enter your opening balance:"))

    data1=(name,acc,dob,add,ph,op_bal)
    data2=(name,acc,op_bal)

    sql1=("insert into account values(%s,%s,%s,%s,%s,%S)")
    sql2=("insert into amount values(%s,%s,%s)")

    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)

    mydb.commit()
    print("data entered successfully")
    main()

def deposit():
    amount=input("enter the amount to deposite:")
    acc=input("enter your acc no:")
    a="select balance from amount where acc no=%s"
    data1=(acc,)
    x=mydb.cursor()
    x.execute(a,data1)
    result=x.fetchone()
    t=result[0]+amount
    sql=('update amount set balance set balance where acc_no=%s')
    d=(t,acc)
    x.execute(sql,d)
    mydb.commit()
    print('..............................')
    main()
def withdraw():
    amount=input("enter the amount to withdraw:")
    acc=input("enter your acc no:")
    a="select balance from amount where acc_no=%s"
    data1=(acc,)
    x=mydb.cursor()
    x.execute(a,data1)
    result=x.fetchone()
    t=result[0]-amount
    sql=("update amount set balance where acc_bal=%s")
    d=(t,acc)
    x.execute(sql,d)
    mydb.commit()
    print('.................................')
    main()
def balance():
    ac=input("enter the account no:")
    a="select * from amount where acc_no is=%s"
    data=(ac,)
    x=mydb.cursor()
    x=execute(a,data)
    mydb.commit()

def main():
    print('''
          1. open new account
          2. deposite amount
          3. withdraw amount
          4. balance enquiry
          5. show customer details
          6. close the account
          ''')
    choose=int(input('choose your option:'))
    match choose:
               case 1:
                    print("open new account")
                    open()
               case 2:
                    print("deposite amount")
                    deposite()
               case 3:
                    print("withdraw amount")
                    withdraw()
               case 4:
                    print("balance enquiry")
                    bal_enq()
               case 5:
                    print("show customer details")
                    cust_details()
               case 6:
                    print("close  an account")
                    close()
               case _:
                    print("enter an invalid number")
                    main()
main()
               
