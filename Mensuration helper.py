user=''
while user!='exit':
    shape=input("Enter a 2D shape(Triangle,Rectangle,Square,Circle) or 'exit'to Exit:")
    if shape =='Triangle':
        opn=input("What Function do you want to do(Area,Perimeter):")
        if opn=='Area':
            b=int(input("Enter Base:"))
            h=int(input("Enter Height:"))
            print("Area of Triange=",(b*h)/2)
        elif opn=='Perimeter':
            side1=int(input("Enter First Side:"))
            side2=int(input("Enter Second Side:"))
            side3=int(input("Enter Third Side:"))
            print("Perimter of Triangle=",side1+side2+side3)    
    if shape=='Rectangle':
        opn=input("What Function do you want to do(Area,Perimeter):")
        if opn=='Area':
            l=int(input("Enter Length:"))
            b=int(input("Enter Base:"))
            print("Area of Rectangle=",l*b)
        elif opn=='Perimeter':
            l1=int(input("Enter Length:"))
            b1=int(input("Enter Base:"))
            print("Perimeter of Rectangle=",2*(l1*b1))
    if shape=='Square':
        opn=input("What Function do you want to do(Area,Perimeter):")
        if opn=='Area':
            side=int(input("Enter Side:"))
            print("Area of Square=", side*side)
        elif opn=='Perimeter':
            side=int(input("Enter Side:"))
            print("Perimeter of Square",4*side)
    if shape=='Circle':
        if opn=='Area':
            r=int(input("Enter Radius:"))
            print("Area of Circle:",3.14*r*r)
        if opn=='Perimeter':
            r=int(input("Enter Radius:"))
            print("Perimeter of Circle=",2*3.14*r)
    if shape=='exit':
        break

