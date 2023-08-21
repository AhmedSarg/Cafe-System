import sqlite3
import sys
sys.path.insert(0, "classes")
from product import Product


def openConnection():
    connection = sqlite3.connect("database\cafe.db")
    print("connection opened")
    return connection


def endConnection(connection):
    connection.close()
    print("connection ended")


def addClient(connection, client):
    cursor = connection.cursor()
    cursor.execute(
        """
        insert into Customer(Name, Phone, Address) values (?, ?, ?)
        """,
        (client.name, client.phone, client.address),
    )
    connection.commit()


def getMenu(connection, category):
    cursor = connection.cursor()
    result = cursor.execute("select * from Product where category = ?", ([category])).fetchall()
    products = list()
    for product in result:
        if product[0] != 0:
            products.append(Product(id=product[0], name=product[1], category=product[2], price=product[3]))
    connection.commit()
    return products

