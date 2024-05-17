import numpy as np

def calculate(val):
    # checking the length of the list
    np_val = 0 # initialising the numpy variable

    if len(val) == 9:
        np_val = np.array(val)
    else:
        raise ValueError("List must contain nine numbers.")

    # checking the data type of the numpy array
    if np_val.dtype in ['int','float']:
        pass
    else:
        print('There is a non-number in the array')

    # reshaping the initial array to 3x3 matrix
    np_val = np_val.reshape(3,3)

    # initialising the dictionary
    calculations = {}

    # calculating mean values
    calculations['mean'] = [np_val.mean(axis=0).tolist(),
                    np_val.mean(axis=1).tolist(),
                    np_val.flatten().mean()]

    calculations['variance'] = [np_val.var(axis=0).tolist(),
                        np_val.var(axis=1).tolist(),
                        np_val.flatten().var()]

    calculations['standard deviation'] = [np_val.std(axis=0).tolist(),
                                    np_val.std(axis=1).tolist(),
                                    np_val.flatten().std()]

    calculations['max'] = [np_val.max(axis=0).tolist(),
                    np_val.max(axis=1).tolist(),
                    np_val.flatten().max()]

    calculations['min'] = [np_val.min(axis=0).tolist(),
                    np_val.min(axis=1).tolist(),
                    np_val.flatten().min()]

    calculations['sum'] = [np_val.sum(axis=0).tolist(),
                    np_val.sum(axis=1).tolist(),
                    np_val.flatten().sum()]

    return calculations