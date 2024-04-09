def is_perfect(num):
    i =num-1
    sum = 0
    my_list = []
    while i>1 :
        if num %i ==0:
            my_list.append(i)
            sum +=i
        i-=1
    if sum == num:
        print(str(num) + " is a perfect number :)")
        return sum
    else : 
        print(str(num) + "is not a perfect number its divisors are: ")
        print(my_list)
        return sum

