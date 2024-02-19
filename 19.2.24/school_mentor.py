
print("1.print the abc in uppercase or lowercase.")
print("2.print a word starting with a specific letter.")
print("3.print N*N multiplication table.")
print("4.print square number of a given number.")
print("5. check if a given number is prime.")
words=[
    "Apple","Butterfly","Castle","Dolphin","Elephant","Firefly","Guitar","Horizon","Iceberg","Jaguar","Kangaroo","Lighthouse","Moonlight","Nebula","Octopus","Penguin","Quasar","Rainbow","Starfish","Telescope","Umbrella","Volcano","Waterfall","Xenon","Yellowjacket","zebra"]
choice = input("please choose a function from 1 to 5: ")
print ('hello')
match choice:
    case '1':
        list_ = []  
        for i in range(97, 123):  
            list_.append(chr(i))  
        for i in range(65, 91):  
            list_.append(chr(i))  
  
        print(list_) 
    case '2':
        choosen_letter = input("please choose a letter: ").lower()
        print(words[ord(choosen_letter)-97])
    case '3':
        choosen_num = input("please choose a number: ")
        for i in range (1,int(choosen_num)+1):
            for j in range(1,int(choosen_num)+1):
                print(i*j,end=' ')
            print("")
    case '4':
        choosen_num = input("please choose a number: ")
        num = int(choosen_num)
        val = num*num
        print(val)
    case '5':
        choosen_num= input("please enter a number: ")
        num = int(choosen_num)
        flag = False
        for i in range (2,num):
            if num%i==0:
                flag =True
        if flag == True:
            print("the number you choose is not a prime number")
        else:
            print("the number you choose is a prime number")


