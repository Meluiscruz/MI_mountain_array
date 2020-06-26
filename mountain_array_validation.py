# -*- coding: utf-8 -*-

#The following list is listed some arrays that could be (or not) Mountain Arrays.

Array_list = [[0,2,3,4,5,2,1,0], [1,2,3,1], [1,2,3,4,5], [5,4,3,2,1], [1,2,3,4,4,4,5,0], [1,2,3,4,5,4,3,2,1], [2,1],[0,3,2,1], [3,5,5]]

Array_Validation = False

def run():
    for array in Array_list:
        N = len(array)
        idx = 0
        top_index=array.index(max(array))
        #First, check if the peak is not at the extremes of the array.
        if top_index == 0 or top_index == (N-1):
            Array_Validation = False
        else:
            #Climb-up the array
            while idx + 1 < (N - 1) and array[idx] < array[idx+1]:
                idx += 1
                if array[idx] == array[idx+1]:
                    Array_Validation = False
            #Walk-down the array
            while idx + 1 < (N - 1) and array[idx] > array[idx+1]:
                idx += 1
                if array[idx] == array[idx+1]:
                    Array_Validation = False
                else:
                    Array_Validation = True
        if Array_Validation:
            print(f'This array: {array} is a Mountain Array')
        else:
            print(f'This array: {array} is NOT a Mountain Array')

if __name__ == '__main__':
    run()