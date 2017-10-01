import random
import matplotlib.pyplot as plt
import io

def generate(data):

    a = random.randint(20, 100)
    histo = [random.randint(1, 100) for i in range(a)]
    data['params']['histo'] = histo
    #plt.hist(histo)
    #data["params"]["a"] = a
 
    data["correct_answers"]["a"] = a

    return data
    


def file(data):
    if data['filename']=='figure.png':
        plt.hist(data['params']['histo'], bins =10, histtype='bar', ec='black')
        plt.xlabel("Student's Scores (out of 100)")
        plt.ylabel("Number of Students in Score Range")
        plt.title("Distribution of Students by Exam Scores")
        buf = io.BytesIO()
        plt.savefig(buf,format='png')
        return buf
