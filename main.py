# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import copy

# 0    1    2  3   4
# PC1  PC2   X  Y  turn
# 1    1    0  0   A
init = list("1100A")
q_print = []
q_calc = []
exist = []

q_print.append(init)
q_calc.append(init)
exist.append(init)


def loop_queue(q_cal):
    temp_q_cal = []
    while len(q_cal) != 0:
        node = q_cal.pop(0)
        node1 = copy.deepcopy(node)
        node2 = copy.deepcopy(node)
        # T1
        #goto step1 : PC1
        if (node1[0] == '1'):
            node1[2] = '1'
            node1[0] = '2'
        elif (node1[0] == '2'):
            node1[4] = 'B'
            node1[0] = '3'
        elif (node1[0] == '3'):
            if (node1[3] == '1' and node1[4] == 'B'):
                print("do nothing")
            else:
                node1[0] = '4'
        elif (node1[0] == '4'):
            node1[2] = '0'
            node1[0] = '1'
        else:
            assert (0)
        if (node1 not in exist):
            q_print.append(node1)
            temp_q_cal.append(node1)
            exist.append(node1)
        # T2
        if (node2[1] == '1'):
            node2[3] = '1'
            node2[1] = '2'
        elif (node2[1] == '2'):
            node2[4] = 'A'
            node2[1] = '3'
        elif (node2[1] == '3'):
            if (node2[2] == '1' and node2[4] == 'A'):
                print("do nothing")
            else:
                node2[0] = '4'
        elif (node2[1] == '4'):
            node2[3] = '0'
            node2[1] = '1'
        if (node2 not in exist):
            q_print.append(node2)
            temp_q_cal.append(node2)
            exist.append(node2)
    return temp_q_cal


def main_func():
    main_temp_queue = loop_queue(q_calc)
    while (len(main_temp_queue) != 0):
        t = loop_queue(main_temp_queue)
        main_temp_queue = t
    length = len(q_print)
    i=0
    while i<length:
        print(q_print[i])
        i=i+1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_func()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
