import pymysql

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='112358@Hm$',
        database='pokemons_schema'
    )
