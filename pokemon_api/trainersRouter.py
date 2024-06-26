from fastapi import APIRouter, HTTPException
import pymysql
from db_manager import database as db
import requests

trainer_router = APIRouter()

@trainer_router.get("/trainers/{trainer_name}/pokemons/")
def get_pokemons_by_trainer(trainer_name: str):
    connection = db.get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT p.name FROM pokemons p
                JOIN pokemon_ownership po ON p.id = po.pokemon_id
                JOIN trainers t ON t.id = po.trainer_id
                WHERE t.name = %s
            """, (trainer_name,))
            result = cursor.fetchall()
        if not result:
            raise HTTPException(status_code=404, detail="No pokemons found for the given trainer")
        return [row[0] for row in result]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()

@trainer_router.delete("/trainers/{trainer_name}/pokemons/{pokemon_name}")
def delete_pokemon_from_trainer(trainer_name: str, pokemon_name: str):
    connection = db.get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                DELETE po FROM pokemon_ownership po
                JOIN trainers t ON t.id = po.trainer_id
                JOIN pokemons p ON p.id = po.pokemon_id
                WHERE t.name = %s AND p.name = %s
            """, (trainer_name, pokemon_name))
        connection.commit()
        return {"message": "Pokemon deleted from trainer successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()

@trainer_router.post("/trainers/{trainer_name}/pokemons/{pokemon_name}")
def add_pokemon_to_trainer(trainer_name: str, pokemon_name: str):
    connection = db.get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM trainers WHERE name=%s", (trainer_name,))
            trainer = cursor.fetchone()
            if not trainer:
                raise HTTPException(status_code=404, detail="Trainer not found")
            trainer_id = trainer[0]
            
            cursor.execute("SELECT id FROM pokemons WHERE name=%s", (pokemon_name,))
            pokemon = cursor.fetchone()
            if not pokemon:
                raise HTTPException(status_code=404, detail="Pokemon not found")
            pokemon_id = pokemon[0]
            
            cursor.execute("""
                SELECT * FROM pokemon_ownership 
                WHERE trainer_id=%s AND pokemon_id=%s
            """, (trainer_id, pokemon_id))
            if cursor.fetchone():
                raise HTTPException(status_code=400, detail="Trainer already owns this Pokemon")
            
            cursor.execute(
                "INSERT INTO pokemon_ownership (pokemon_id, trainer_id) VALUES (%s, %s)",
                (pokemon_id, trainer_id)
            )
        connection.commit()
        return {"message": "Pokemon added to trainer successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()

@trainer_router.post("/trainers/{trainer_name}/pokemons/{pokemon_name}/evolve")
def evolve_pokemon(trainer_name: str, pokemon_name: str):
    connection = db.get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM trainers WHERE name=%s", (trainer_name,))
            trainer = cursor.fetchone()
            if not trainer:
                raise HTTPException(status_code=404, detail="Trainer not found")
            trainer_id = trainer[0]
            

            # Check if any pokemons with the given name exist
            cursor.execute("SELECT id FROM pokemons WHERE name=%s", (pokemon_name,))
            pokemons = cursor.fetchall()
            if not pokemons:
                raise HTTPException(status_code=404, detail="Pokemon not found")
            
            
              
        # Check ownership for each matching pokemon
            pokemon_ids = [pokemon[0] for pokemon in pokemons]
            flag= False
            for pokemon in pokemon_ids:  
                cursor.execute("""
                    SELECT * FROM pokemon_ownership 
                    WHERE trainer_id=%s AND pokemon_id=%s
                """, (trainer_id, pokemon))
                if cursor.fetchone():
                    flag= True
                    to_evolve = pokemon
                    #return f"Trainer with ID {trainer_id} owns Pokemon with ID {pokemon}"
            if flag == False : 
                raise HTTPException(status_code=400, detail=f"Trainer with ID {trainer_id} does not own any Pokemon named {pokemon_name}")

            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}')
            if response.status_code != 200:
                raise HTTPException(status_code=500, detail="Error fetching evolution data")
            species_url = response.json()['species']['url']
            
            species_response = requests.get(species_url)
            if species_response.status_code != 200:
                raise HTTPException(status_code=500, detail="Error fetching species data")
            evolution_chain_url = species_response.json()['evolution_chain']['url']
            
            evolution_chain_response = requests.get(evolution_chain_url)
            if evolution_chain_response.status_code != 200:
                raise HTTPException(status_code=500, detail="Error fetching evolution chain data")
            evolution_chain = evolution_chain_response.json()['chain']
            
            def find_evolution(chain, current_pokemon):
                if chain['species']['name'] == current_pokemon:
                    return chain['evolves_to'][0]['species']['name'] if chain['evolves_to'] else None
                for sub_chain in chain['evolves_to']:
                    result = find_evolution(sub_chain, current_pokemon)
                    if result:
                        return result
                return None
            
            evolved_pokemon_name = find_evolution(evolution_chain, pokemon_name.lower())
            if not evolved_pokemon_name:
                raise HTTPException(status_code=400, detail=f"{pokemon_name} cannot evolve further")
            
            cursor.execute("SELECT id FROM pokemons WHERE name=%s", (evolved_pokemon_name,))
            evolved_pokemon = cursor.fetchone()
            if not evolved_pokemon:
                raise HTTPException(status_code=404, detail="Evolved Pokemon not found in database")
            evolved_pokemon_id = evolved_pokemon[0]
            
            cursor.execute("""
                UPDATE pokemon_ownership 
                SET pokemon_id=%s 
                WHERE trainer_id=%s AND pokemon_id=%s
            """, (evolved_pokemon_id, trainer_id, to_evolve))
        connection.commit()
        return {"message": f"{pokemon_name} evolved to {evolved_pokemon_name} successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()
