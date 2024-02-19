main_number_list= []
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            return False
    return True
for i in range(4,150):
    main_number_list.append(i)
prime_numbers_list = []
for i in range (2,4):
    prime_numbers_list.append(i)
    j=1
    while i*j<150:
        if i*j in main_number_list:
            main_number_list.remove(i*j)
        j+=1
    for num in main_number_list:
        if is_prime(num):
            prime_numbers_list.append(num)
            j=1
            while num*j<150:
                if num*j in main_number_list:
                    main_number_list.remove(num*j)
                j+=1
        
print(prime_numbers_list)
print("the prime list is: ")
print(prime_numbers_list)


 
