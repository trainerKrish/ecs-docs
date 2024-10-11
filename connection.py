import mysql.connector


def create_connection():
    cnx = mysql.connector.connect(
        user='root',
        password='my-secret',
        host='db-mysql',
        database='mysql'
    )

    cur = cnx.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS user_table (
        username text,
        password text,
        name text,
        age int
    )""")

    cur.execute("INSERT INTO user_table VALUES ('karl', 'pwd', 'Karl', 16)")
    cur.execute("INSERT INTO user_table VALUES ('krish', 'pwd2', 'Krish', 96)")

    cnx.commit()
    cnx.close()
