import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS User(
ID INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(1, 11):
    cursor.execute('INSERT INTO User (username, email, age, balance) VALUES(?,?,?,?)',
                   (f'User{i}', f'example{i}@gmail.com', f'{10 * i}', '1000'))
for i in range(1, 11, 2):
    cursor.execute('UPDATE User SET balance = ? WHERE username = ? ', (500, f'User{i}'))
for i in range(1, 11, 3):
    cursor.execute('DELETE FROM User WHERE username = ? ', (f'User{i}',))
connection.commit()
connection.close()
