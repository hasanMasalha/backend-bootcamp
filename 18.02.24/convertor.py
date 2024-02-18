scource = input('enter the scource type ')
val = float(input('enter the value'))
match scource:
    case 'C':
         print((val*1.8) + 32)
    case 'F':
         print((val-32)/1.8)
    case 'MPH':
         print(val*1.609)
    case 'KPH':
        print(val/1.609)
   #case KG:
   #     action-1
   #case stone:
   #     action-2
   #case lbs:
   #     action-3
 