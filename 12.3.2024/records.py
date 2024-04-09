import csv
from numpy import False_
import records
import sys
import datetime




class records:
    def __init__(self,name,num):
        self.name = name
        self.num = num

def open_records(records):
    file = open('records.csv')
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)
    return rows


def add_records(to_add,to_add_num, records_list: list):
    flag = False 
    for record in records_list:
        if record[0] == to_add:
            flag = True
            record[1]+=to_add_num
    if flag == False:
        records_list.append([to_add,to_add_num])
def delete_record(to_delete,to_delete_num,records_list: list):
    for record in records_list:
        if record[0] == to_delete:
            if record[1] <  to_delete_num :
                print("sorry you dont have this number of records")
            elif record[1] > to_delete_num:
                records[1]-=to_delete_num
                print("the records deleted succesfully")
            elif record[1] == to_delete_num:
                records_list.remove(record)
                print("the records deleted succesfully")

def search_by_name(name, recors_list: list):
    flag= False
    for record in recors_list:
        if name in record[0]:
            flag = True
            return record
    if flag == False:
        print("sorry I didnt found a record that includes this name ")

def update_name(old_name, new_name, record_list: list):
    record = search_by_name(old_name,record_list)
    record[0] = new_name
    record_list.remove(search_by_name(old_name,record_list))
    record_list.append(record)
    print("name has been updated")
def update_quantity(name, new_quantity, record_list: list):
    record = search_by_name(name,record_list)
    record[1] = new_quantity
    record_list.remove(search_by_name(name,record_list))
    record_list.append(record)
    print("quantity has been updated successfully ")
def get_sum(record_list):
    sum=0
    for record in record_list:
        sum+= record[1]
    return sum
def sorting_records(record_list):
    sorted_list = sorted(record_list)
    return sorted_list




if __name__ == "__main__":
#C:/Users/hasan/backend-bootcamp/backend-bootcamp/12.3.2024/try.csv
    records_list = []
    with open(sys.argv, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
    
        next(csv_reader)
    
        for row in csv_reader:
            record_name = row[0]
            amount = int(row[1])
            print(f"Record: {record_name}, Amount: {amount}")
            records_list.append(row)

    print("1.add a record")
    print("2.delete a record")
    print("3.search by name")
    print("4.update name")
    print("5.update quantity")
    print("6.sum of all records")
    print("7.sort the records")
    print("8.Exit")
    choice = input("please choose a number from 1 to 8 depending on what you want to do")
    while choice != 8:
        match choice:


            case "1":
                name = input("please enter the name of the record you want to add: ")
                quantity = input("please add the quantity of this record: ")
                add_records(name,quantity, records_list)
                current_time = datetime.datetime.now()
                with open("log.txt", "w") as file1:
                    file1.write(quantity +" of record " + name + " has been added at " +current_time )
            case "2":
                name = input("please enter the name of the record you want to delete:")
                quantity = input("please add the quantity of this record: ")
                delete_record(name,quantity,records_list)
                current_time = datetime.datetime.now()
                with open("log.txt", "w") as file1:
                    file1.write(quantity +" of record " + name + " has been deleted at " +current_time )
            case "3":
                name = input("please enter the name of the record you want to search:")
                search_by_name(name,records_list)
                current_time = datetime.datetime.now()
                with open("log.txt", "w") as file1:
                    file1.write("searched for record " + name + current_time )
            case "4":
                name = input("please enter the name of the record you want to update:")
                new_name = input("please enter the new name of the record:")
                update_name(name,new_name,records_list)
                current_time = datetime.datetime.now()
                with open("log.txt", "w") as file1:
                    file1.write("record" + name + "was updated to "+ new_name +"at" + current_time )
            case "5":
                name = input("please enter the name of the record you want to update:")
                new_quantity = input("please enter the new quantity of the record:")
                update_quantity(name,new_quantity,records_list)
                current_time = datetime.datetime.now()
                with open("log.txt", "w") as file1:
                    file1.write("quantity of record " + name  +"was updated to " + new_quantity + "at" + current_time )
            case "6":
                get_sum(records_list)
                current_time = datetime.datetime.now()
                with open("log.txt", "w") as file1:
                    file1.write("sum was asked for at " + current_time )
            case "7":
                sorting_records(records_list)
                current_time = datetime.datetime.now()
                with open("log.txt", "w") as file1:
                    file1.write("records were sorted at " + current_time )
        

