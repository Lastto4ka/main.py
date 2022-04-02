import math
def main():
    f1=1
    f2=1
    f3=2
    x=1
    n=1
    while (abs(f1-x)<0.001) :
        x=(math.pow(((1 + math.sqrt(5)) / 2),(n+1))-math.pow(((1 - math.sqrt(5)) / 2),(n+1))) / math.sqrt(5)
        f1=f2
        f2=f3
        f3=f2+f1
        n += 1
    print("Начиная с",n-1,"числа Фибоначчи, истинные значения отличаются больше чем на 0.001 ")

if __name__ == '__main__':
    main()