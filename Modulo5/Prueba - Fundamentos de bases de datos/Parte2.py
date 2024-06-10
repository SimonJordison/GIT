import psycopg2

# Datos de conexión
db_params = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "Flow",
    "host": "localhost",
    "port": "5432"
}

# Nombre de la nueva base de datos
new_dbname = "preguntas_respuestas_db"

# Conectar a la base de datos PostgreSQL
conn = psycopg2.connect(**db_params)
conn.autocommit = True
cur = conn.cursor()

# Crear la base de datos (si no existe)
cur.execute(f"CREATE DATABASE {new_dbname}")

# Cerrar la conexión inicial y conectar a la nueva base de datos
cur.close()
conn.close()

# Actualizar los parámetros de conexión para la nueva base de datos
db_params["dbname"] = new_dbname
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

# Crear las tablas
cur.execute("""
    CREATE TABLE Usuarios (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(255),
        edad INT,
        CHECK (edad >= 18)
    );
""")

cur.execute("""
    CREATE TABLE Preguntas (
        id SERIAL PRIMARY KEY,
        pregunta VARCHAR(255),
        respuesta_correcta VARCHAR(255)
    );
""")

cur.execute("""
    CREATE TABLE Respuestas (
        id SERIAL PRIMARY KEY,
        respuesta VARCHAR(255),
        usuario_id INT REFERENCES Usuarios(id) ON DELETE CASCADE,
        pregunta_id INT REFERENCES Preguntas(id)
    );
""")

# Insertar usuarios
usuarios = [
    (1, "Usuario 1", 25),
    (2, "Usuario 2", 30),
    (3, "Usuario 3", 22),
    (4, "Usuario 4", 27),
    (5, "Usuario 5", 19)
]
cur.executemany("INSERT INTO Usuarios (id, nombre, edad) VALUES (%s, %s, %s)", usuarios)

# Insertar preguntas
preguntas = [
    (1, "Pregunta 1", "Respuesta A"),
    (2, "Pregunta 2", "Respuesta B"),
    (3, "Pregunta 3", "Respuesta C"),
    (4, "Pregunta 4", "Respuesta D"),
    (5, "Pregunta 5", "Respuesta E")
]
cur.executemany("INSERT INTO Preguntas (id, pregunta, respuesta_correcta) VALUES (%s, %s, %s)", preguntas)

# Insertar respuestas
respuestas = [
    (1, "Respuesta A", 1, 1),  # Correcta para Pregunta 1 por Usuario 1
    (2, "Respuesta A", 2, 1),  # Correcta para Pregunta 1 por Usuario 2
    (3, "Respuesta B", 3, 2),  # Correcta para Pregunta 2 por Usuario 3
    (4, "Respuesta Incorrecta", 4, 3),  # Incorrecta para Pregunta 3
    (5, "Respuesta Incorrecta", 5, 4)   # Incorrecta para Pregunta 4
]
cur.executemany("INSERT INTO Respuestas (id, respuesta, usuario_id, pregunta_id) VALUES (%s, %s, %s, %s)", respuestas)

# Confirmar los cambios
conn.commit()

# Contar las respuestas correctas por usuario
cur.execute("""
    SELECT u.nombre, COUNT(r.id) as num_respuestas_correctas
    FROM Usuarios u
    LEFT JOIN Respuestas r ON u.id = r.usuario_id
    LEFT JOIN Preguntas p ON r.pregunta_id = p.id
    WHERE r.respuesta = p.respuesta_correcta
    GROUP BY u.id
""")
print("Cantidad de respuestas correctas por usuario:")
for row in cur.fetchall():
    print(f"{row[0]} tiene {row[1]} respuestas correctas")

# Contar las respuestas correctas por pregunta
cur.execute("""
    SELECT p.pregunta, COUNT(r.id) as num_respuestas_correctas
    FROM Preguntas p
    LEFT JOIN Respuestas r ON p.id = r.pregunta_id
    WHERE r.respuesta = p.respuesta_correcta
    GROUP BY p.id
""")
print("Cantidad de respuestas correctas por pregunta:")
for row in cur.fetchall():
    print(f"{row[0]} tiene {row[1]} respuestas correctas")

# Borrar un usuario y demostrar borrado en cascada
cur.execute("DELETE FROM Usuarios WHERE id = 1")
conn.commit()

# Contar las respuestas después de borrar un usuario
cur.execute("""
    SELECT u.nombre, COUNT(r.id) as num_respuestas_correctas
    FROM Usuarios u
    LEFT JOIN Respuestas r ON u.id = r.usuario_id
    LEFT JOIN Preguntas p ON r.pregunta_id = p.id
    WHERE r.respuesta = p.respuesta_correcta
    GROUP BY u.id
""")
print("Cantidad de respuestas correctas por usuario después de borrar un usuario:")
for row in cur.fetchall():
    print(f"{row[0]} tiene {row[1]} respuestas correctas")

# Alterar la tabla de usuarios para agregar el campo email con restricción única
cur.execute("""
    ALTER TABLE Usuarios
    ADD COLUMN email VARCHAR(255) UNIQUE
""")
conn.commit()

# Cerrar la conexión
cur.close()
conn.close()
