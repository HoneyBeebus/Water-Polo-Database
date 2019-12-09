#--------PROPERTY OF C. HENRY WHITE-------------------
import sqlite3

from pip._vendor.distlib.compat import raw_input

connect = sqlite3.connect('TPCH.db')
cursor = connect.cursor()

def table_Create():
    cursor.execute("""CREATE TABLE IF NOT EXISTS warehouse (
                                                            w_warehousekey decimal(3,0) not null, 
                                                            w_name char(25) not null,
                                                            w_supplierkey decimal(2,0) not null,
                                                            w_capacity decimal(6,2) not null,
                                                            w_address carchar(40) not null,
                                                            w_nationkey decimal(2, 0) not null);""")

def table_DataFill():
    cursor.execute("""INSERT INTO warehouse (w_warehousekey, w_name, w_supplierkey, w_capacity, w_address, w_nationkey) values (?, ?, ?, ?, ?, ?)""", ((0, 'Warehouse#000000001', 5, 20, 'Oxford Street, London, England', 4)))
    connect.commit()

def table_Insert():
    Name = input("Name: ")
    supplier = input("Supplier: ")
    Capacity = input("Capacity: ")
    Address = input("Address: ")
    nation = input("Nation: ").upper()

    print()

    cursor.execute("SELECT s_suppkey FROM supplier WHERE s_name = ?", (supplier,))
    suppkey = cursor.fetchone()

    cursor.execute("SELECT n_nationkey FROM nation WHERE n_name = ?", (nation,))
    nationkey = cursor.fetchone()

    cursor.execute("SELECT MAX(w_warehousekey) FROM warehouse")
    currentMaxKey = cursor.fetchone()

    if suppkey is not None and nationkey is not None:
        cursor.execute("""INSERT INTO warehouse (w_warehousekey, w_name, w_supplierkey, w_capacity, w_address, w_nationkey)
                            values (?, ?, ?, ?, ?, ?)""",((currentMaxKey[0] + 1), Name, suppkey[0], Capacity, Address, nationkey[0])
                       )
        connect.commit()
    else:
        print("ERROR: CANNOT INSERT DUE TO INVALID NATIONKEY OR SUPPKEY")
        print()

def table_Print():
    cursor.execute("SELECT * FROM warehouse")
    print("Printing Table WAREHOUSE at current iteration")
    for row in cursor:
        print(row)
    print()

def query_1():
    print("Question 1: Find the supplier with the smallest number of warehouses.")
    print("Solution: ")
    cursor.execute("""SELECT DISTINCT s_name FROM supplier, warehouse WHERE w_supplierkey = s_suppkey and w_capacity = (SELECT MIN(w_capacity) FROM warehouse) """)
    print(cursor.fetchall())
    print()

def query_2():
    print("Question 2: Find the maximum warehouse capacity across all the suppliers.")
    print("Solution: ")
    cursor.execute("SELECT MAX(w_capacity) FROM warehouse")
    print(cursor.fetchall())
    print()

def query_3():
    print("Question 3: List all the warehouses in Europe with capacity smaller than a given value.")
    cursor.execute("SELECT DISTINCT w_name FROM warehouse, region, nation where w_nationkey = n_nationkey AND n_regionkey = r_regionkey and w_capacity < ?", (input("Give a value: "),))
    print("Solution: ")
    print(cursor.fetchall())
    print()

def query_4():
    sec = connect.cursor()
    print("Question 4: For a supplier name of given name, find whether all its warehouses are capable to fit all its products.")
    sn = raw_input("Give a name: ")
    cursor.execute("SELECT SUM(w_capacity) FROM warehouse, supplier WHERE s_name = ? AND w_supplierkey = s_suppkey", (sn,))
    x = cursor.fetchone()
    sec.execute("SELECT SUM(ps_availqty) FROM partsupp, supplier WHERE s_name = ? AND ps_suppkey = s_suppkey", (sn,))
    y = sec.fetchone()
    print("Solution: ")
    if x > y:
        print("There is enough space!")
    elif x < y:
        print("There is NOT enough space!")
    print()

def query_5():
    print("Question 5: For a nation of given name, print all the warehouses in that country, in descending order of their capacity.")
    cursor.execute("SELECT DISTINCT w_name, w_capacity FROM warehouse, nation WHERE w_nationkey = n_nationkey AND n_name = ? ORDER BY w_capacity DESC", (input("Give a name: ").upper(),))
    print("Solution: ")
    print(cursor.fetchall())
    print()

def query_6():
    print("Question 6: Supplier#000000002 is acquired by Supplier#000000001. Update the warehouse table to reflect this change in ownership. The actual names of the suppliers are taken as input from the user, they are not constants.")
    cursor.execute("SELECT w_supplierkey FROM warehouse WHERE w_supplierkey = ?", (input("Give a supplier name: "),))
    print("Solution: ")
    print(cursor.fetchall())
    print()

print()
table_Create()
table_DataFill()
insert_Bool = input("Would you like to input data into the new warehouse table? (yes or no): ").lower()
if insert_Bool == "yes":
    table_Insert()

table_Print()

qt = input("Would you like to run queries on the TPCH database? (yes or no): ")
print()
if qt == "yes":
    query_1()
    c1 = input("Continue to query? (yes or no): ").lower()
    print()
    if c1 == "yes":
        query_2()
        c2 = input("Continue to query? (yes or no): ").lower()
        print()
        if c2 == "yes":
            query_3()
            c3 = input("Continue to query? (yes or no): ").lower()
            print()
            if c3 == "yes":
                query_4()
                c4 = input("Continue to query? (yes or no): ").lower()
                print()
                if c4 == "yes":
                    query_5()
                    c5 = input("Continue to query? (yes or no): ").lower()
                    print()
                    if c5 == "yes":
                        query_6()
print()
cursor.close()
connect.close()
print("Disconnected from database!!!!!!")
