#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
        my_list_res = []
        for n in range(list_length):
                res = 0
                try:
                        res = my_list_1[n] / my_list_2[n]
                except ZeroDivisionError:
                        print("division by 0")
                except TypeError:
                        print("wrong type")
                except IndexError:
                        print("out of range")
                finally:
                        my_list_res.append(res)
        return my_list_res
