scource = input('enter the scource type ')
val = float(input('enter the value'))
match scource:
    case 'C':
         print((val*1.8) + 32)
    case 'F':
         print((val-32)/1.8)
    case 'MPH':
         print(val/1.6)
    case 'KPH':
          print(val*1.6)
    case 'KG':
         print( "stone" + val/6.5)
         print("lbs" + val*2.204)
    case 'stone':
          print( "lbs" + val/0.071)
          print("KG" + val/0.15)
    case 'lbs':
          print( "stone" + val/14)
          print("KG" + val/2.204)
 