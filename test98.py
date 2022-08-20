import time
import random

def search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

if __name__=='__main__':
    l = [1, 3, 5, 10, 12]
    target = 10
    print(search(l, target))
    
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))
    
    start = time.time()
    for target in sorted_list:
        search(sorted_list, target)
    end = time.time()
    print("Search time:", (end - start)/length, "seconds")