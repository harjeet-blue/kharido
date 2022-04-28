import mysql.connector
mydb  = mysql.connector.connect(host = "127.0.0.1",user = "root" , passwd = "Sarthak@2019",database = "dbms")

mycur = mydb.cursor()

def get_tables():
        mycur.execute("show tables")
        result = mycur.fetchall()
        print(result)
        return result
def get_cloths():
        mycur.execute("select * from clothing")
        result = mycur.fetchall()
        print(result)
        return result
def get_cosmetics():
        mycur.execute("select * from cosmetics")
        result = mycur.fetchall()
        print(result)
        return result
def get_eatables():
        mycur.execute("select * from eatables")
        result = mycur.fetchall()
        print(result)
        return result
def get_electronics():
        mycur.execute("select * from supplier")
        result = mycur.fetchall()
        print(result)
        return result
def get_Customers():
        mycur.execute("select * from Customer")
        result = mycur.fetchall()
        print(result)
        return result
def get_Branch():
        mycur.execute("select * from branch")
        result = mycur.fetchall()
        print(result)
        return result
def get_Employee():
        mycur.execute("select * from employee")
        result = mycur.fetchall()
        print(result)
        return result
def get_Suppliers():
        mycur.execute("select * from supplier")
        result = mycur.fetchall()
        print(result)
        return result
def get_Query1():
        mycur.execute("Select Count(*) from customer group by Customer_Type order by count(*) desc")
        result = mycur.fetchall()
        print(result)
        return result
def get_Query2():
        mycur.execute("Select Count(*) from Contains where Quantity > 2000")
        result = mycur.fetchall()
        print(result)
        return result
def get_Query3():
        mycur.execute("Select C.Customer_ID from Customer C,_order O,cart Ca,contains Co,product P where C.Customer_ID = O.Customer_ID and O.Cart_ID = Ca.Cart_ID and Ca.Cart_ID = Co.Cart_ID and Co.Product_ID = P.Product_ID and P.product_name = 'Gold Tea' And C.Customer_ID in (Select Customer_ID from Customer where Customer_Type = 'Gold')")
        result = mycur.fetchall()
        print(result)
        return result
def get_Query4():
        mycur.execute("Select Ca.Cart_ID from Cart as Ca,Contains as Co where Ca.Cart_ID = Co.Cart_ID and exists(select * from Product P where P.product_ID = Co.Product_ID and P.product_Type = 'Clothing') and exists (select * from Product P where P.product_ID = Co.Product_ID and P.product_Type = 'Eatables')")
        result = mycur.fetchall()
        print(result)
        return result
def get_Query5():
        mycur.execute("Select Min(Date_Of_Appointment) from Works_for Natural Join Employee group by Employee_Role")
        result = mycur.fetchall()
        print(result)
        return result
def get_Query6():
        mycur.execute("Select E.Employee_ID from Employee E ,Increment I where E.Employee_ID = I.Employee_ID and exists (Select Employee_ID from Increment I1 where I.Employee_ID = E.Employee_ID and I.amount != I1.amount)")
        result = mycur.fetchall()
        print(result)
        return result
def get_Query7():
        mycur.execute("Select Avg(Amount) from Cart Natural Join _Order where _Order.discount<= 20")
        result = mycur.fetchall()
        print(result)
        return result
def get_Query8():
        mycur.execute("Select Avg(Amount) from Cart Natural Join _Order group by _Order.Discount having Discount >=20")
        result = mycur.fetchall()
        print(result)
        return result
def get_Query9():
        mycur.execute("Select Employee_ID from Delivers where Delivery_status = 'not delivered'")
        result = mycur.fetchall()
        print(result)
        return result
def get_Query10():
        mycur.execute("update Increment set amount = 10000, date_of_increment = curdate() where Employee_ID in (select W.Employee_ID from works_for as W where 2022 - year(W.Date_of_appointment) > 6)")
        result = mycur.fetchall()
        print(result)
        return result


