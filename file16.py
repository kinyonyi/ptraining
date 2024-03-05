#sqlite3
import sqlite3
import json

conn = sqlite3.connect("myData.db")
print("Database connected")
#will try connecting if exists else creates the database

#creation of the staff table 
try:
    conn.execute("""
        CREATE TABLE staff(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name CHAR(100) NOT NULL,
            rank CHAR(100) NOT NULL,
            age INTEGER NOT NULL,
            salary REAL NOT NULL
        )""")
except sqlite3.OperationalError as e:
    print(f"Error {e}")

#CRUD

def InsertData(name, rank, age, salary):
    conn.execute(f"INSERT INTO staff (name, rank, age, salary) \
        VALUES ('{name}', '{rank}', {age}, {salary}) \
        ")
    conn.commit()
    print("data inserted!")

#InsertData("micheal", "pc", 35, 20000.00)
    
def retrieveData():
    all_data = []
    data = conn.execute("SELECT * FROM staff").fetchall()
    for x in data:
        all_data.append({
            "id": x[0],
            "name": x[1],
            "age": x[2],
            "salary": x[3]
        })

    return all_data

data = retrieveData()
f = open("myData.txt", "w")
f.writelines(json.dumps(data, indent=2))
f.close()
#print(json.dumps(data, indent=2))

def updateData(idValue, field, value):
    conn.execute(f"UPDATE staff SET {field} = '{value}' WHERE id = {idValue}")
    conn.commit()
    return f"{conn.total_changes} made!"

print(updateData(1, "name", "surgical"))
data = retrieveData()
print(json.dumps(data, indent=2))

def deleteData(id):
    conn.execute(f"DELETE FROM staff WHERE id = {id}")
    conn.commit()
    return f"{conn.total_changes} items deleted!"

print(deleteData(2))
data = retrieveData()
print(json.dumps(data, indent=2))

def dropTable():
    conn.execute("DROP TABLE staff")
    conn.commit()
    return "table deleted!"

print(dropTable())