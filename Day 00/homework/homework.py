# hw1

def hw1(a,b,c):
    if a % c == 0 and b % c != 0:
        return int(b - a) // c + 1
    else:
        return int(b - a) // c
    


print(hw1(12,19,3))
print(hw1(1,20,2))



# hw2
def hw2(num,b):
    num = str(num)
    lists1 = []
    lists2 = []
    if "." in str(num):
        num = num.split(".")
        num1 = num[0][::-1]
        num2 = num[1]
        for i in range(len(num1)):
            lists1.append(int(num1[i]) * (b ** i))
        
        for x in range(len(num2)):
            lists2.append(int(num2[x]) * (1 / b ** (x+1)))
        return sum(lists1 + lists2)
        

    else:
        num = num[::-1]
        for i in range(len(num)):
            lists1.append(int(num[i]) * (b ** i))
    
    return sum(lists1)


print(hw2(1011,16))
print(hw2(520.3,6))



# a,b,c,d,e

def hw3(a,b,c,d,e):
    if a > b:
        if a > c:
            if a > d:
                if a > e:
                    return "a"
                else:
                    return "e"
            else:
                if d > e:
                    return "d"
                else:
                    return "e"
        else:
            if c > d:
                if c > e:
                    return "c"
                else:
                    return "e"
            else:
                if d > e:
                    return "d"
                else:
                    return "e"
    else:
        if b > c:
            if b > d:
                if b > e:
                    return "b"
                else:
                    return "e"
            else:
                if d > e:
                    return "d"
                else:
                    return "e"
        else:
            if c > d:
                if c > e:
                    return "c"
                else:
                    return "e"
            else:
                if d > e:
                    return "d"
                else:
                    return "e"
                

print(hw3(1,2,3,4,5))