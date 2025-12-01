if __name__ == "__main__":
    num = input()
    
    list = []
    
    for i in num:
        N = int(i)
        list.append(N)
        
    list.sort(reverse=True)

    for i in list:
        print(i, end='')
    
    print()