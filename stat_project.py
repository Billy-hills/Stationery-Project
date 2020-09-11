print("---------------------Stationery Project------------------")
import mysql.connector
import sys
db=input("Do you have database ? (y/n)=")
dbname=""
mydb=""
mycursor=""
if (db=='n' or db=='N'):
    dname=input("Enter new Database name u want to create=")
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1prathamcool")
    mycursor=mydb.cursor()
    mycursor.execute("create database "+ dname)
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1prathamcool",database=dname)
    mycursor=mydb.cursor()
    mycursor.execute("create table item(Name_of_item char(50),QRcode char(50) primary key,Purchasing_Price int,Selling_Price int,Quantity_in int,Quantity_sold int)")
    print("Student Table Automatically Created in",dname," Database")
    print("\n-----Its Open for other Operations Now--------")
elif(db=='y'or db=='Y'):
    dname=input("Enter existing Database name u want to open=")
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1prathamcool",database=dname)
    print("\n-------Its Open for other Operations Now--------")
else:
    sys.stderr.write("Enter a valid input !!")
while (True):
    print('''\n\nPress=
1)Add Stock
2)See all Stock
3)See any particular Stock item using Item_Code/Item_Name
4)Delete Stock item using Item_Code/Item Name
5)See Availabe stock of particular item using Item_Code/Item Name
6)Exit''')
    ch=int(input("Enter your choice="))
    if (ch==6):
        print("Bye")
        break
    elif (ch==1):
        print("----Add Stock----")
        n=input("Enter item name=")
        c=input("Enter item code=")
        p=input("Enter purchasing price=")
        s=input("Enter selling price=")
        qi=input("Enter Quantity in=")
        qs=input("Enter Quantity sold=")
        sql="Insert into item values(%s,%s,%s,%s,%s,%s)"
        val=(n,c,p,s,qi,qs)
        mycursor=mydb.cursor()
        mycursor.execute(sql,val)
        mydb.commit()
        print("------Record Saved----")
        
    elif (ch==2):
        mycursor=mydb.cursor()
        mycursor.execute("select * from item")
        myresult=mycursor.fetchall()
        t=mycursor.rowcount
        if (t!=0):
            print("Item_Name    QR_CODE    Purchasing_Price    Selling_Price  Quantity_in        Quantity_Out")
            for x in myresult:
                print(x[0],"     ",x[1],"     ","₹",x[2],"          ","₹",x[3],"             ",x[4],"pc.","             ",x[5],"pc.")
        else:
            sys.stderr.write("Empty,Add Record first!!\n\n")
    elif (ch==3):
        n=input("What u want to enter,Item_Name/Code (n/c)or (name/code)=")
        if (n=="name" or n=="Name" or n=='n'):
            r=input("Enter Item_Name which u want to see=")
            mycursor=mydb.cursor()
            mycursor.execute(" select * from item where Name_of_item="+"'"+r+"'")
            myresult=mycursor.fetchall()
            t=mycursor.rowcount
            if (t!=0):
                print("Item_Name    QR_CODE    Purchasing_Price    Selling_Price  Quantity_in        Quantity_Out")
                for x in myresult:
                    print(x[0],"     ",x[1],"     ","₹",x[2],"          ","₹",x[3],"             ",x[4],"pc.","             ",x[5],"pc.")
            else:
                sys.stderr.write("Record doent exist,check Item_Name!\n")
        elif (n=="code" or n=="Code" or n=='c'):
            r=input("Enter Item_Code which u want to see=")
            mycursor=mydb.cursor()
            mycursor.execute(" select * from item where QRcode="+'"'+r+'"')
            myresult=mycursor.fetchall()
            t=mycursor.rowcount
            if (t!=0):
                print("Item_Name    QR_CODE    Purchasing_Price    Selling_Price  Quantity_in        Quantity_Out")
                for x in myresult:
                    print(x[0],"     ",x[1],"     ","₹",x[2],"          ","₹",x[3],"             ",x[4],"pc.","             ",x[5],"pc.")
            else:
                sys.stderr.write("Record doent exist,check Item_Code!")
        else:
            sys.stderr.write("Enter a valid Input!!\n")
    elif (ch==4):
        n=input("What u want to enter,Item_Name/Code (n/c)or (name/code)=")
        if (n=="name" or n=="Name" or n=='n'):
            r=input("Enter Item_Name which u want to delete=")
            mycursor=mydb.cursor()
            mycursor.execute(" delete from item where Name_of_item="+"'"+r+"'")
            mydb.commit()
            t=mycursor.rowcount
            if (t!=0):
                print("Found,and Successfully Deleted\n")
            else:
                sys.stderr.write("Record doent exist,check Item_Name!")
        elif (n=="code" or n=="Code" or n=='c'):
            r=input("Enter Item_Code which u want to delete=")
            mycursor=mydb.cursor()
            mycursor.execute(" delete from item where QRcode="+"'"+r+"'")
            mydb.commit()
            t=mycursor.rowcount
            if (t!=0):
                print("Found,and Successfully Deleted\n")
            else:
                sys.stderr.write("Record doent exist,check Item_Code!\n")
        else:
            sys.stderr.write("Enter a valid Input!!\n")
    elif (ch==5):
        n=input("What u want to enter,Item_Name/Code (n/c)or (name/code)=")
        if (n=="name" or n=="Name" or n=='n'):
            r=input("Enter Item_Name which u want to see=")
            mycursor=mydb.cursor()
            mycursor.execute(" select Quantity_in,Quantity_sold,(Quantity_in-Quantity_sold) from item where Name_of_item="+"'"+r+"'")
            myresult=mycursor.fetchall()
            t=mycursor.rowcount
            if (t!=0):
                print("Stock_in     Stock_sold    Quantity_left")
                for x in myresult:
                    print(x[0],"pc.","     ",x[1],"pc.","     ",x[2],"pc.")
            else:
                sys.stderr.write("Record doent exist,check Item_Name!")
        elif (n=="code" or n=="Code" or n=='c'):
            r=input("Enter Item_Code which u want to see=")
            mycursor=mydb.cursor()
            mycursor.execute(" select Quantity_in,Quantity_sold,(Quantity_in-Quantity_sold) from item where QRcode="+"'"+r+"'")
            myresult=mycursor.fetchall()
            t=mycursor.rowcount
            if (t!=0):
                print("Stock_in     Stock_sold    Quantity_left")
                for x in myresult:
                    print(x[0],"pc.","     ",x[1],"pc.","     ",x[2],"pc.")
            else:
                sys.stderr.write("Record doent exist,check Item_Code!")
        else:
            sys.stderr.write("Enter a valid Input!!\n")
input()
                
            
            
            
    
        
                
            
            
    
        
        
        
        
        
