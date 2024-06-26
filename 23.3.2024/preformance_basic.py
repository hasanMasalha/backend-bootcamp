import time

def search_num_in_list(mylist : list,num : int):
    for i in mylist:
        if i == num:
            return "found it"
        
def search_num_in_list2(mylist: list, num: int):
    mylist.sort
    start= 0 
    end = len(mylist)
    mid = int(end/2)
    print(type(mid))
    while start < end:
        if mylist[mid] > num:
            end = mid
            mid = int((end - start)/2)
        elif mylist[mid] < num:
            start = mid
            mid = int((end - start)/2)
        elif mylist[mid] == num:
            return "found it" 



num = 5
mylist = [1,7,9,9,4,5,6,3,2,1,7,8,9,4,9,215,266,53,987,621,1,6]
start_time = time.time()
search_num_in_list2(mylist, num)
end_time = time.time()
run_time = end_time-start_time
print("the time is: "+ str(run_time ))
start_time = time.time()
search_num_in_list(mylist, num)
end_time = time.time()
run_time = end_time-start_time
print("the time is: "+ str(run_time) )