from PIL import Image  
input_image = Image.open("C:/Users/hasan/backend-bootcamp/backend-bootcamp/24.3.2024/img1.jpg") 
pixel_map = input_image.load() 
width, height = input_image.size 
  
# taking half of the width: 
for i in range(width): 
    for j in range(height): 
     r,g,b = (input_image.getpixel((i, j)) )
     pixel_map[i, j] = (255-r,255-g,255-b)
     

