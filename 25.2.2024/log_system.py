import datetime


def log_messages(message, level, timestamp,event):
    to_return= {}
    def add_message(message):
        if message == None:
              return "" 
        return " ["+message+"]"
    def add_level(level): 
        if level == None:
            return ""
        return " ["+level+"]"
    def add_timestamp(timestamp):
        if timestamp == None:
              return ""
        return " ["+datetime.datetime.now().isoformat()+"]"
    def add_event(event):
        if event == None:
             return ""
        return " ["+event+"]"
    to_return[message] = add_message(message)
    to_return[level]= add_level(level)
    to_return[timestamp]= add_timestamp(timestamp)
    to_return[event]=add_event(event)
    return to_return

logs = [log_messages(message ="This is a simple message", level=None,timestamp=None, event=None),
log_messages(message="This is a warning message", level="error", timestamp = None, event= None),
log_messages(message="This message has a timestamp",level = "info", timestamp=True,event = None ),
log_messages(message="This message has event data",level = None,timestamp = True, event="ATTACK")]


print("for no date log press 1.")
print("for logs with date press 2.")
print("for logs with a timestamp range press 3. ")
print("for a short msg log press 4")
inp = input("")
match inp:
    case "1":
          for log in logs:
               if log["timestamp"] == None:
                    print(log)
    case "2":
          for log in logs:
               if log["timestamp"] != None:
                    print(log)
    case "3": 
        range1 = input("please enter the min date you want to get")
        range2 = input("please enter the max date you want to get")

        for log in logs:
            if log["timestamp"] < range and log["timestamp"]< range2 :
                 print(log)
    case 4:
        for log in logs: 
            if len(log["message"])<10: 
                print(log)