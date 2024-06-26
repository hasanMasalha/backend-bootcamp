import json
def save_user_data_db(username,hashed_password):
    db = load_db()
    print(db)
    db = update_db_new_user(db,username,hashed_password)
    print(db)
    save_updated_db(db)
    print('current_db: ', db)
    

def load_db():
        with open('C:/Users/hasan/backend-bootcamp/backend-bootcamp/server_auth_try/data/users_data.json','r') as f:
            db = f.read()
            db1 = json.loads(db)
            return db1
        
def update_db_new_user(db,username,hashed_password):
    db[username] = {
        "username": username,
        "password": hashed_password
   }
    print(db)
    return db
def save_updated_db(db):
    db_serializable = convert_bytes_to_serializable(db)
    with open('C:/Users/hasan/backend-bootcamp/backend-bootcamp/server_auth_try/data/users_data.json','w') as f:
        json.dump(db_serializable, f)


def convert_bytes_to_serializable(data):
    if isinstance(data, bytes):
        return data.decode('utf-8')  # Assuming bytes data is UTF-8 encoded
    elif isinstance(data, dict):
        return {key: convert_bytes_to_serializable(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_bytes_to_serializable(item) for item in data]
    else:
        return data