import math


test_h=int(input("Area of the height"))
test_w=int(input("Area of the widhth"))
coverage = 5

def paint_cal(height=test_h,widht=test_w,coverage=coverage):
    area = height * widht 
    number_of_cans = math.ceil(area / coverage)
    print(f"numer of cans required is {number_of_cans}")

paint_cal()




