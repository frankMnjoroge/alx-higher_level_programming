#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
     no = 0

     for y in range(x):
        try:
            print(my_list[y], end="")
            no += 1
        except IndexError:
            break
    print("")
    Return(no)
