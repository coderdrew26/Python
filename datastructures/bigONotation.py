import time

def take_first(my_list):
    return my_list[0]

short_list = [13, 25, 42]
tic = time.perf_counter()
first = take_first(short_list)
toc = time.perf_counter()
print(first)
print(toc-tic)