import sqlite3

with sqlite3.connect('library.db') as conn:
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''CREATE TABLE IF NOT EXISTS authors
                      (id INTEGER PRIMARY KEY, name TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS books
                      (id INTEGER PRIMARY KEY, title TEXT, author_id INTEGER,
                      FOREIGN KEY (author_id) REFERENCES authors(id))''')

    authors = [
        ('Ліна Костенко',),
        ('Леся Українка',),
        ('Іван Франко',)
    ]

    cursor.executemany("INSERT INTO authors (name) VALUES (?)", authors)

    books = [
        ('Маруся Чурай', 1),
        ('Бояриня', 2),
        ('Захар Беркут', 3)
    ]
    cursor.executemany("INSERT INTO books (title, author_id) VALUES (?, ?)", books)

    cursor.execute('''SELECT books.title, authors.name
                      FROM books
                      INNER JOIN authors ON books.author_id = authors.id''')
    inner_join_result = cursor.fetchall()
    print("Результат INNER JOIN:")
    for row in inner_join_result:
        print(row)

    cursor.execute('''SELECT books.title, authors.name
                      FROM books
                      LEFT JOIN authors ON books.author_id = authors.id''')
    left_join_result = cursor.fetchall()
    print("Результат LEFT JOIN:")
    for row in left_join_result:
        print(row)

    cursor.execute('''SELECT books.title, authors.name
                      FROM books
                      FULL JOIN authors ON books.author_id = authors.id''')
    full_join_result = cursor.fetchall()
    print("Результат FULL JOIN:")
    for row in full_join_result:
        print(row)

