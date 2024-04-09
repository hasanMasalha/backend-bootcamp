
this_list =[]
def check(num):
    sum = 0
    while i>1 :
        if num %i ==0:
            sum +=i
        i-=1
    return sum
num = input("please enter a number: ")

def find(num):
    this_list.append(num)
    result =check(num)

    if result in this_list:
        print("the result of the divisors is already in out list ")
    else:
        this_list.append(result)
        find(result)

