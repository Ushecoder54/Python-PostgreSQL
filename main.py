import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="12345", port=5432)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS person (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender CHAR
);

""")

cur.execute("""INSERT INTO person (id, name, age, gender) VALUES
(1, 'Mike', 35, 'm')
(2, 'John', 36, 'm')
(3, 'Greg', 37, 'm')
(4, 'Scott', 38, 'm')
(5, 'Themba', 39, 'm')
""")

cur.execute("""SELECT * FROM person WHERE name = 'Greg';""")

print(cur.fetchone())

cur.execute("""SELECT * FROM person WHERE age < 50;""")

for row in cur.fetchall()
    print(row)


sql = cur.mogrify("""SELECT * FROM person WHERE starts_with(name, %s) AND age < %s;""" ("G", 50))

print(sql)

cur.execute(sql)

print(cur.fetchall())

conn.commit()

cur.close()
conn.close()