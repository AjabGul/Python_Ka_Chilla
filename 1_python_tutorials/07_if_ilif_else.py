marks = int(input("inter your marks? "))

if marks > 100 or marks < 0:
    print('Invalid marks enterd')
elif marks >= 85:
    print('GPA = 4 and Grad = A')
elif 80 <= marks <= 84:
    print('GPA = 3.66 and Grad = -A')
elif 75 <= marks <= 79:
    print('GPA = 3.33 and Grad = +B')
elif 71 <= marks <= 74:
    print('GPA = 3.00 and Grad = B')
elif 68 <= marks <= 70:
    print('GPA = 2.66 and Grad = -B')
elif 64 <= marks <= 67:
    print('GPA = 2.00 and Grad = +C')
elif 61 <= marks <= 63:
    print('GPA = 1.66 and Grad = C')
elif 58 <= marks <= 60:
    print('GPA = 1.30 and Grad = -C')
elif 54 <= marks <= 57:
    print('GPA = 1.00 and Grad = +D')
elif 50 <= marks <= 53:
    print('GPA = 3.66 and Grad = D')
else:
    print('Fail')
