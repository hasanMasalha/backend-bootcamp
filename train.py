# def get_min_and_max(mylist: list):
#     min= mylist[0]
#     max = mylist[0]
#     for item in mylist:
#         if item < min:
#             min = item
#         if item > max:
#             max = item
#     return min, max 

# def max_devide_with_five(mylist: list):
#     max =mylist[0]
#     for item in mylist:
#         if item % 5 ==0 and item > max:
#             max = item
#     return max 
# def get_(mylist: list, callback):
#     for item in mylist:
        

# test_list= [1,2,3,0,5]
# test_list2= [0,1,5,15,16,24,-6] 
# print(get_min_and_max(test_list))
# print(max_devide_with_five(test_list2))

import json

def get_students():
    studentsList = []
    try:
        with open('C:/Users/hasan/backend-bootcamp/backend-bootcamp/ramzor/db.json', 'r') as f:
            file_content = f.read()
            json_object = json.loads(file_content)
            for student in json_object:
                studentsList.append(student['name'])
            print(studentsList)
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format in the file.")

get_students()
