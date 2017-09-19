import random
import matplotlib.pyplot as plt
import io
import numpy as np

def generate(data):

    a = random.randint(10, 30)
    histo = [random.randint(1, 10) for i in range(a)]
    data['params']['histo'] = histo
    median = np.median(histo)
    mean = np.mean(histo)
    if(median>mean){
        data["params"]["ans_correct"] = "median"
        data["params"]["ans_false1"] = "mean"
        data["params"]["ans_false2"] = "equal"
        }
    elif(mean > median){
        data["params"]["ans_false1"] = "median"
        data["params"]["ans_correct"] = "mean"
        data["params"]["ans_false2"] = "equal"
    }
    elif(mean == median){
        data["params"]["ans_false2"] = "median"
        data["params"]["ans_false1"] = "mean"
        data["params"]["ans_correct"] = "equal"
    }
    #plt.hist(histo)
    #data["params"]["a"] = a
 
    #data["correct_answers"]["a"] = a

    return data
    


def file(data):
    if data['filename']=='figure.png':
        plt.hist(data['params']['histo'])
        buf = io.BytesIO()
        plt.savefig(buf,format='png')
        return buf
