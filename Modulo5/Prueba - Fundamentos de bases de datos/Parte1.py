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
new_dbname = "peliculas_db"

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
    CREATE TABLE Peliculas (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(255),
        anno INT
    );
""")

cur.execute("""
    CREATE TABLE Tags (
        id SERIAL PRIMARY KEY,
        tag VARCHAR(32)
    );
""")

# Insertar películas
peliculas = [
    (1, "Pelicula 1", 2021),
    (2, "Pelicula 2", 2022),
    (3, "Pelicula 3", 2023),
    (4, "Pelicula 4", 2024),
    (5, "Pelicula 5", 2025)
]
cur.executemany("INSERT INTO Peliculas (id, nombre, anno) VALUES (%s, %s, %s)", peliculas)

# Insertar tags
tags = [
    (1, "Tag1"),
    (2, "Tag2"),
    (3, "Tag3"),
    (4, "Tag4"),
    (5, "Tag5")
]
cur.executemany("INSERT INTO Tags (id, tag) VALUES (%s, %s)", tags)

# Asignar tags a películas en Python
peliculas_tags = {
    1: [1, 2, 3],  # Película 1 tiene 3 tags
    2: [4, 5]     # Película 2 tiene 2 tags
}

# Contar los tags por película en Python
tag_counts = {pelicula[0]: 0 for pelicula in peliculas}
for pelicula_id, tags in peliculas_tags.items():
    tag_counts[pelicula_id] = len(tags)

# Obtener los nombres de las películas
cur.execute("SELECT id, nombre FROM Peliculas")
pelicula_nombres = {row[0]: row[1] for row in cur.fetchall()}

# Mostrar los resultados
for pelicula_id, count in tag_counts.items():
    print(f"{pelicula_nombres[pelicula_id]} tiene {count} tags")

# Cerrar la conexión
cur.close()
conn.close()
