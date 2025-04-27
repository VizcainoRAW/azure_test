import mysql.connector

# Datos de conexión
config = {
    'host': 'dbtasktest.mysql.database.azure.com',
    'port': 3306,
    'user': 'ivan',
    'password': 'Qwerty1234',  # Cambia {your-password} por tu contraseña real
    'database': 'tasksDB',
    'ssl_disabled': False            # Para que use SSL
}

# Conexión a la base de datos y consulta
try:
    conexion = mysql.connector.connect(**config)

    if conexion.is_connected():
        print("✅ Conexión exitosa a la base de datos en Azure.")

        cursor = conexion.cursor()

        # Consulta para traer todos los datos de la tabla tasks
        consulta = "SELECT * FROM tasks;"
        cursor.execute(consulta)

        # Recuperar todos los registros
        resultados = cursor.fetchall()

        print("\n📋 Resultados de la tabla 'tasks':")
        print("-" * 40)
        for fila in resultados:
            id, name, state = fila
            estado = "Completa" if state else "Pendiente"
            print(f"ID: {id}, Nombre: {name}, Estado: {estado}")

except mysql.connector.Error as error:
    print(f"❌ Error de conexión o ejecución: {error}")

finally:
    # Cierre de conexión
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("\n🔒 Conexión cerrada.")
