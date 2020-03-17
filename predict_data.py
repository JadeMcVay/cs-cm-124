from fill_data import fill_data
import numpy as np

def predict_data(imported_data, filled_data, pred_data):
    genome, people = fill_data(imported_data, filled_data)
    geno_data = np.loadtxt(filled_data).reshape(genome, people)
    geno_data = geno_data.astype(int)
    haplo_pred = []
    for value in range(genome):
        for person in range(people):
            if geno_data[value, person] == 0:
                haplo_pred.append([0,0])
            elif geno_data[value, person] == 1:
                haplo_pred.append([0,1])
            elif geno_data[value, person] == 2:
                haplo_pred.append([1,1])
            else:
                print('you done goofed!')
    haplo_pred = np.asarray(haplo_pred)
    haplo_pred = haplo_pred.reshape(genome, people*2)
    np.savetxt(pred_data, haplo_pred, fmt='%s') 