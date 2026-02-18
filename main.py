import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Создание таблицы (без комментария внутри SQL для чистоты)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        grade INTEGER,
        city TEXT
    )
''')

# Данные для вставки
students = [
    ('Иван', 18, 5, 'Москва'),
    ('Ольга', 19, 4, 'Казань'),
    ('Сергей', 20, 5, 'Самара'),
    ('Мария', 18, 3, 'Омск'),
    ('Анна', 21, 4, 'Тула'),
    ('Павел', 22, 5, 'Пермь'),
    ('Юлия', 20, 3, 'Томск'),
    ('Андрей', 19, 4, 'Сочи'),
    ('Виктор', 18, 5, 'Уфа'),
    ('Светлана', 21, 4, 'Воронеж')
]

# Вставка нескольких записей
cursor.executemany('''
    INSERT INTO Students (name, age, grade, city) VALUES (?, ?, ?, ?)
''', students)

# --- Запросы SELECT ---

# 1. Студенты с оценкой 5
cursor.execute('SELECT name FROM Students WHERE grade = 5')
print("Студенты с оценкой 5:")
for row in cursor.fetchall():
    print(row[0])

# 2. Студенты с оценкой 4
cursor.execute('SELECT name FROM Students WHERE grade = 4')
print("Студенты с оценкой 4:")
for row in cursor.fetchall():
    print(row[0])

# 3. Студенты с оценкой 3
cursor.execute('SELECT name FROM Students WHERE grade = 3')
print("Студенты с оценкой 3:")
for row in cursor.fetchall():
    print(row[0])

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
