check_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
num = []
length = 0
tmp = 0

def ipt():
    global num, length, tmp
    tmp = int(input())
    num = list(map(int, str(tmp)))
    length = len(num)

def firstDigit():
    global length
    k = length-1
    common = k * 10**(k-1)
    zero = k * 10**(k-1) - (10**k - 1)//9
    check_list[0] = zero
    for i in range(1, 10):
        check_list[i] = common          # 0 ~09999999999

    for i in range(1, num[0]):
        check_list[i] += 10**(length-1) #   10000000000 ~(num[0]-1)999999999999
        for j in range(0, 10):
            check_list[j] += common

def check(i):
    global length
    k = length-1-i
    if(k==0):
        for j in range(0, num[i]+1):
            check_list[j] += 1
        for j in range(0, length-1):
            check_list[num[j]] += num[i]+1

    else:
        if(num[i]==0):
            return
        else:
            common = k * 10**(k-1)
            for j in range(0, i):
                check_list[num[j]] += (num[i]) * (10**(length-i-1))
            for j in range(0, num[i]):
                for q in range(0, 10):
                    check_list[q] += common
                check_list[j] += 10**(length-1-i)

def short():
    global check_list, tmp
    for i in range(1, tmp+1):
        result = []
        result = list(map(int, str(i)))
        for j in result:
            check_list[j] += 1

if __name__ == "__main__":
    ipt()
    if(length < 2):
        short()
    else:
        firstDigit()
        for i in range(1, length):
            check(i)

    print(*check_list)