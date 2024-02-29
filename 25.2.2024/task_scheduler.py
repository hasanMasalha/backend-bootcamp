working_dict={
    "sunday" : [],
    "monday": [],
    "Tuesday":[],
    "Wednesday":[],
    "Thursday": [],
}
def request():
task_name = input("please enter the name ")
task_day= input("please choose the day of the task")
task_start= input ("please enter what time the task starts")
task_duration = input("please enter the task duration")

print("when you done please Enter S to stop")

while task_name != "s" :
    if  task_start not in working_dict ["task_day"]:
        for i in range(task_start,task_start+task_duration):
            working_dict ["task_day"].append([task_name,i])
    else: 
        rewrite = input("the time you insered is already taken do you want to rescheduler press R if you want to continue anyway press C: ")
        if rewrite == "C":
            request()
