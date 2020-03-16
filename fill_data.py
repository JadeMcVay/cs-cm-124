import numpy as np

def fill_data(imported_data, exported_data):
    f = open(imported_data, 'r')
    masked_lines = f.readlines()
    masked_data=[]
    for x in masked_lines:
        masked_data.append(x.split(' '))
    f.close()
    
    masked_data = np.asarray(masked_data)
    
    people = masked_data.shape[1]
    genome = masked_data.shape[0]
    count_stars = []
    count_zeros = []
    count_twos = []
    for value in range(genome):
        count_zero = 0
        count_two = 0
        for person in range(people - 1):
            if masked_data[value, person] == '0':
                count_zero += 1
            if masked_data[value, person] == '2':
                count_two += 1
        count_zeros.append(count_zero)
        count_twos.append(count_two)
        
    data = masked_data
    for value in range(genome):
        for person in range(people):
            if masked_data[value, person] == '*' or masked_data[value, person] == '*\n':
                if (count_zeros[value] > count_twos[value]):
                    data[value, person] = '0'
                if (count_zeros[value] < count_twos[value] or count_zeros[value] == count_twos[value]):
                    data[value, person] = '2'
                    
    np.savetxt(exported_data, masked_data, fmt='%s') 
    
    return(masked_data.shape)