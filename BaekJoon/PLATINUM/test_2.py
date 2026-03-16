check_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
num = 0

def ipt():
    global num
    num = int(input())

def check(n):
    global check_list
    result = []
    result = list(map(int, str(n)))
    for i in result:
        check_list[i] += 1


if __name__ == "__main__":
    ipt()
    for i in range(1, num+1):
        check(i)
    
    print(*check_list)