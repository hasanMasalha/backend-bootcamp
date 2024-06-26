from fastapi import APIRouter, HTTPException
from schemas import PokemonSchema
import pymysql
from db_manager import database as db
import requests

pokemon_router = APIRouter()

@pokemon_router.get("/pokemons/")
def get_pokemons_by_type(pokemon_type: str):
    connection = db.get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM pokemons WHERE type=%s", (pokemon_type,))
            result = cursor.fetchall()
        if not result:
            raise HTTPException(status_code=404, detail="No pokemons found with the given type")
        return [row[0] for row in result]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()

@pokemon_router.post("/pokemons/")
def add_pokemon(pokemon: PokemonSchema):
    connection = db.get_db_connection()
    try:
        with connection.cursor() as cursor:
            for poke_type in pokemon.types:
                cursor.execute(
                    "INSERT INTO pokemons (name, type, height, weight) VALUES (%s, %s, %s, %s)",
                    (pokemon.name, poke_type, pokemon.height, pokemon.weight)
                )
        connection.commit()
        return {"message": "Pokemon added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()

@pokemon_router.get("/pokemons/{pokemon_name}/trainers/")
def get_trainers_of_pokemon(pokemon_name: str):
    connection = db.get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT t.name FROM trainers t
                JOIN pokemon_ownership po ON t.id = po.trainer_id
                JOIN pokemons p ON p.id = po.pokemon_id
                WHERE p.name = %s
            """, (pokemon_name,))
            result = cursor.fetchall()
        if not result:
            raise HTTPException(status_code=404, detail="No trainers found for the given pokemon")
        return [row[0] for row in result]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()
