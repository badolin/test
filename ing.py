import numpy as np

def mutual_information(arr):
    # check if it is 0
    if(np.count_nonzero(arr) == np.size(arr)):
        p_i = np.sum(arr, axis = 0)
        p_j = np.sum(arr, axis = 1)
        log_p_i = np.log(p_i)
        log_p_j = np.log(p_j)
        log_arr = np.log(arr)
        x1 = np.sum(arr * log_arr)
        x2 = np.sum(p_i * log_p_i)
        x3 = np.sum(p_j * log_p_j)
        x = x1 - x2 -x3
        return x
    # check if there is a negative number
    elif(np.amin(arr) < 0):
        return "wrong data. cannot calculate ln from 0 and negative numbers"
    else:
        return "wrong data. cannot calculate ln from 0"
