import sqlite3


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
