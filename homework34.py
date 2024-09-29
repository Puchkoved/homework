import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('DELETE FROM User WHERE username = ? ', ('User6',))
cursor.execute('SELECT COUNT(*) FROM User')
total_users = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM User')
all_balances = cursor.fetchone()[0]
print(all_balances/total_users)


connection.commit()
connection.close()