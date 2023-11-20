#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for y in range(list_length):
        try:
            divs = my_list_1[y] / my_list_2[y]
        except TypeError:
            print("wrong type")
            divs = 0
        except ZeroDivisionError:
            print("division by 0")
            divs = 0
        except IndexError:
            print("out of range")
            divs = 0
        finally:
            n_list.append(divs)
    return n_list
