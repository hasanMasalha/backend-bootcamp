import json
from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    classes: list

def add_student(student1: Student):
    flag = True
    try:
        with open('C:/Users/hasan/backend-bootcamp/backend-bootcamp/ramzor/db.json', 'r') as f:
            json_object = json.load(f)
            for item in json_object:
                if item["id"] == student1.id:
                    flag = False
                    break
            if not flag:
                return "Student already exists."
            else:
                json_object.append(student1.dict())
        with open('C:/Users/hasan/backend-bootcamp/backend-bootcamp/1.4.2024/db.json', 'w') as f:
            json.dump(json_object, f)
        return "Student added successfully."
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format in the file.")

student1 = Student(id=0, name="aa", classes=["math"])
print(add_student(student1))
