import sqlite3
def initiate_db(name):
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute(
        f'''CREATE TABLE IF NOT EXISTS {name}(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL) '''
    )
    connect.commit()
    connect.close()


def get_all_products(name='database.db'):
    connect = sqlite3.connect(name)
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM Products')
    res = cursor.fetchall()
    connect.close()
    return res



def add_db(title, price, description=''):
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    check = cursor.execute(f'SELECT * FROM Products WHERE title=?', (f'{title}',))
    if check.fetchone() is None:
        cursor.execute(
            f'''INSERT INTO Products(title, description, price) VALUES('{title}','{price}','{description}')'''
        )
    connect.commit()
    connect.close()
if __name__ == '__main__':
    print(get_all_products()[0][1])






