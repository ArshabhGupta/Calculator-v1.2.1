import math
import statistics

print("Welcome to the calculator! \n")
print("THIS IS A PRE-RELEASE VERSION!!")

print("What's new? v1.2.1")
print("Added Total Surface Area (TSA) functions \n")

while True:
    print("Choose operation type: ")
    print("1. Basic")
    print("2. Scientific")
    print("3. 2D Shape Functions")
    print("4. Total Surface Area (New)")
    c = int(input("Enter the option number: "))
    if c == 1:
        
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponention")
        print("6. Roots")
        print("7. Factorial")
        print("8. HCF")
        print("9. LCM \n")
    elif c == 2: 
        print("10. Sine")
        print("11. Cosine")
        print("12. Tangent")
        print("13. Arc Sine")
        print("14. Arc Cosine")
        print("15. Arc Tangent")
        print("16. Arithmetic Mean")
        print("17. Median")
        print("18. Mode")
    elif c == 3:
        print("19. Square Area")
        print("20. Rectangle Area")
        print("21. Circle Area")
        print("22. Parallelogram Area")
        print("23. Trapezium Area")
        print("24. Rhombus Area")
        print("25. Isoceles Triangle Area")
        print("26. Scalene Triangle Area")
        print("27. Equilateral Triangle Area")
        print("28. Oval Area")
        print("29. Perimeter of any Quadrilateral")
        print("30. Circle Circumference")
        print("31. Oval Circumference")
        print("32. Perimeter of any Triangle")
        print("33. Semicircle Area")
        print("34. Semicircle Perimeter")
        print("35. Area of Kite")
    elif c == 4:
        print("36. TSA of Cuboid")
        print("37. TSA of Cube")
        print("38. TSA of Sphere")
        print("39. TSA of Cylinder")
        print("40. TSA of Cone")
        print("41. TSA of Triangular Prism")

    choice = int(input("Please enter the option number: "))
    
    if choice == 1:
        a = float(input("Enter a number: "))
        b = float(input("Enter a number: "))
        print(a + b)
    elif choice == 2:
        a = float(input("Enter a number: "))
        b = float(input("Enter a number: "))    
        print(a - b)
    elif choice == 3:
        a = float(input("Enter a number: "))
        b = float(input("Enter a number: "))    
        print(a* b)
    elif choice == 4:
        a = float(input("Enter a number: "))
        b = float(input("Enter a number: "))        
        print(a / b)
    elif choice == 5:
        a = float(input("Enter the base: "))
        b = float(input("Enter the exponent: "))
        print(math.pow(a, b))  
    elif choice == 6:
        a = float(input("Enter a number: "))
        b = float(input("Enter a number: "))
        print(math.pow(a, (1/b)))
    elif choice == 7:
        a = int(input("Enter a number: "))
        print(math.factorial(a))
    elif choice == 8:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        print(math.gcd(a, b))
    elif choice == 9:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        print(math.lcm(a, b))
    elif choice == 10:
        a = float(input("Enter the degrees"))
        math.sin(a)
    elif choice == 11:
        a = float(input("Enter the degrees"))
        math.cos(a)
    elif choice == 12:
        a = float(input("Enter the degrees"))
        math.tan(a)
    elif choice == 13:
        a = float(input("Enter the degrees"))
        math.asin(a)
    elif choice == 14:
        a = float(input("Enter the degrees"))
        math.acos(a)
    elif choice == 15:
        a = float(input("Enter the degrees"))
        math.atan(a)
    elif choice == 16:
        list = eval(input("Enter a list of number in (): "))
        print(statistics.mean(list))
    elif choice == 17:
        list = eval(input("Enter a list of number in (): "))
        print(statistics.median(list))
    elif choice == 18:
        list = eval(input("Enter a list of number in (): "))
        print(statistics.mode(list))
    elif choice == 19:
        a = float(input("Enter the side of the square: "))
        print(a ** 2)
    elif choice == 20:
        l = float(input("Enter the length: "))
        b = float(input("Enter the breadth: "))
        print(l * b)
    elif choice == 21:
        r = float(input("Enter the radius: "))
        print( math.pi * (r ** 2))
    elif choice == 22:
        b = float(input("Enter the base: "))
        h = float(input("Enter the height: "))
        print(b * h)
    elif choice == 23:
        a = float(input("Enter the length of a parallel side: "))
        b = float(input("Enter the length of a parallel side: "))
        h = float(input("Enter the height: "))
        print(1/2 * h (a + b))
    elif choice == 24:
        d1 = float(input("Enter a diagonal: "))
        d2 = float(input("Enter a diagonal: "))
        print(1/2 * d1 * d2)
    elif choice == 25:
        h = float(input("Enter the height: "))
        b = float(input("Enter the base: "))
        print(1/2 * h * b)
    elif choice == 26:
        a = float("Enter the 1st side: ")
        b = float("Enter the 2nd side: ")
        c = float("Enter the 3rd side: ")
        s = (a + b + c)/2
        area = (s(s - a)(s - b)(s - c)) ** 1/2 #Heron's Formula
        print(area)
    elif choice == 27:
        s = float(input("Enter the side: "))
        a = (3 ** 1/2)/4 * (a ** 2)
        print(a)
    elif choice == 28:
        r1 = float(input("Enter the major radius: "))
        r2 = float(input("Enter the minor radius: "))
        a = math.pi * r1 * r2
        print(a)
    elif choice == 29:
        a = float(input("Enter a side: "))
        b = float(input("Enter a side: "))
        c = float(input("Enter a side: "))
        d = float(input("Enter a side: "))
        print(a + b + c + d)
    elif choice == 30:
        r = float(input("Enter the radius: "))
        a = 2 * math.pi * r
    elif choice == 31:
        a = float(input("Enter the major radius: "))
        b = float(input("Enter the minor radius: "))
        h = ((a - b) ** 2) / ((a + b) ** 2)
        a = math.pi * (a + b) * (1 + (3 * h / (10 + ((4 - 3 * h) ** 1/2))))
        print(a)
    elif choice == 32:
        a = float(input("Enter the 1st side: "))
        b = float(input("Enter the 2nd side: "))
        c = float(input("Enter the 3rd side: "))
        print(a + b + c)
    elif choice == 33:
        r = float(input("Enter the radius: "))
        a = (math.pi * r ** 2) / 2
    elif choice == 34:
        r = float(input("Enter the radius: "))
        p = 2 * math.pi * r
        print((p / 2) + 2 * r)
    elif choice == 35:
        d1 = float(input("Enter the diagonal: "))
        d2 = float(input("Enter the diagonal: "))
        print(1/2 * d1 * d2)
    elif choice == 36:
        l = float(input("Enter the length: "))
        b = float(input("Enter the breadth: "))
        h = float(input("Enter the height: "))
        tsa = 2 * ((l * b) * (l * h) * (h * b))
        print(tsa)
    elif choice == 37:
        s = float(input("Enter the side length: "))
        tsa = 6 * (s ** 2)
        print(tsa)
    elif choice == 38:
        r = float(input("Enter the radius: "))
        tsa = 4 * math.pi * (r ** 2)
    elif choice == 39:
        h = float(input("Enter the height: "))
        r = float(input("Enter the radius: "))
        tsa = 2 * math.pi * r * h + 2 * math.pi * (r ** 2)
        print(tsa)
    elif choice == 40:
        r = float(input("Enter the radius: "))
        h = float(input("Enter the height: "))
        l = (h ** 2 + r ** 2) ** (1/2)
        tsa = math.pi * r * (r + l)
        print(tsa)
    elif choice == 41:
        b = float(input("Enter the base breadth: "))
        l = float(input("Enter the base length: "))
        h = float(input("Enter the height: "))
        s1 = eval(input("Enter the triangular side in (): "))
        s = statistics.mean(s1) * 3
        tsa = (s * l) + (b * h)
        print(tsa)
    else:
        print("Invalid choice!")

    x = input("Do you want to retry? (Y/N): ")
    if x == 'Y':
        continue
    else:
        break