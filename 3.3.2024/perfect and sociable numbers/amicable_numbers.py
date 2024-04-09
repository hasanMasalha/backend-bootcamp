import perfect_number
def are_friendly(num1, num2):
    sum1 = perfect_number(num1)
    sum2 = perfect_number(num2)
    if sum1 == num2 and sum2 == num1 :
        print("these numbers are friendly :)")