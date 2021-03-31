import time
import multiprocessing
import numpy as np

def vector_add_cpu(a, b):
    c = np.zeros(a.shape[0], dtype=np.float32)
    for i in range(a.shape[0]):
        c[i] = a[i] + b[i]
    return c

def multiprocessing_func(j, a, b):
    vector_add_cpu(a,b)
    
if __name__ == '__main__':
    NUM_ELEMENTS = 100000000
    NUM_CORES = 6
    
    a_source = np.ones(NUM_ELEMENTS, dtype=np.float32)
    b_source = np.ones(NUM_ELEMENTS, dtype=np.float32)

    starttime = time.time()
    processes = []
    
    a_split = [[] for i in range(NUM_CORES)]
    b_split = [[] for i in range(NUM_CORES)]
    
    a_split = np.array_split(a_source, NUM_CORES)
    b_split = np.array_split(b_source, NUM_CORES)
                
    a_split = np.array(a_split)
    b_split = np.array(b_split)

    for j in range(NUM_CORES):
        p = multiprocessing.Process(target=multiprocessing_func, args=(j, a_split[j], b_split[j], ))
        print("adding process ", j)
        processes.append(p)
    
    for process in processes:
        process.start()
    
    for process in processes:
        process.join()
        
    print()    
    print('Time taken = {} seconds'.format(time.time() - starttime))