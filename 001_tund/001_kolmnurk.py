side_a = float(input("please enter side A:"))
side_b = float(input("please enter side B:"))
side_c = float(input("please enter side C:"))
half_perimeter =(side_a+side_b +side_c)/2
print (half_perimeter)
triangle_area = ((half_perimeter) * (half_perimeter - side_a)
                 * (half_perimeter - side_b)
                 *(half_perimeter - side_c))**0.5
print (triangle_area)

print("Side A = " + str(side_a))
print("Side B = " + str(side_b))
print("Side C = " + str(side_c))
print("Area of triangle is " + str(triangle_area))