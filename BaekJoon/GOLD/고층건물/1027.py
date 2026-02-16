num_list = []
inc_list = []
max_building = 0
max_temp = 0
num = 0

def ipt():
    global num, num_list
    num = int(input())
    num_list = list(map(int, input().split()))

def inc(k):
    global inc_list
    for i in range(0, num):
        if(i < k):
            inc_list.append((num_list[i] - num_list[k])/(k-i))
        elif(i==k):
            inc_list.append(0)
        else:
            inc_list.append((num_list[i] - num_list[k])/(i-k))

def compare(k):
    global max_temp, inc_list
    inc_list.clear()
    max_temp = 0
    inc(k)
    #print(inc_list)
    max_inc = -1000000000
    for j in range(k-1, -1, -1):
        if(inc_list[j]>max_inc):
            max_temp += 1
            #print(k,j,inc_list[j],max_inc)
            max_inc = inc_list[j]
    max_inc = -1000000000
    for j in range(k+1, num):
        if(inc_list[j]>max_inc):
            max_temp += 1
            #print(k,j,inc_list[j],max_inc)
            max_inc = inc_list[j]

    #print(inc_list)
    #print(k)
    return max_temp



if __name__ == "__main__":
    ipt()
    for i in range(0, num):
        tmp = compare(i)
        if(tmp > max_building):
            max_building = tmp
    print(max_building)