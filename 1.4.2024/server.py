from fastapi import FastAPI
import json 
from students import student
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def home():
    return {"data": "students"}
@app.get("/all_students")
def get_students():
    studentsList = []
    try:
        with open('C:/Users/hasan/backend-bootcamp/backend-bootcamp/1.4.2024/db.json', 'r') as f:
            file_content = f.read()
            json_object = json.loads(file_content)
            for student in json_object:
                studentsList.append(student['name'])
            return(studentsList)
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format in the file.")
@app.get("/student/{id}")
def get_student(id):
    with open('C:/Users/hasan/backend-bootcamp/backend-bootcamp/1.4.2024/db.json', 'r') as f:
        content = f.read()
        json_object = json.load(content)
        for student in json_object:
            if str(student["id"]) == str(id):
                return (student["name"])
@app.get("/studentsInClass/{class_id}")
def get_students_in_class(class_id):
    students_list =[]
    with open('C:/Users/hasan/backend-bootcamp/backend-bootcamp/1.4.2024/db.json', 'r') as f:
        content = f.read()
        json_object = json.loads(content)
        for student in json_object:
            if class_id in student["classes"]:
                students_list.append(student["name"])
        return students_list
            
@app.post("/add_student/", response_model=None)
def add_student(student1: student):
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
                json_object.append(student1.model_dump_json())
        with open('C:/Users/hasan/backend-bootcamp/backend-bootcamp/1.4.2024/db.json', 'w') as f:
            json.dump(json_object, f)
        return "Student added successfully."
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format in the file.")

        