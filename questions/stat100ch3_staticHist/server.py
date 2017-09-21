import random
import json

def generate(data):

    num_elements = 5   #  data["options"]["num_elements"] 
    bucket_size = 20
    samples = random.sample(range(10, 40), num_elements)

    ## what follows isn't the most pythonic way of doing this, but it is simpler for 
    ## those that aren't familiar with functional programming
    sample_array = []
    for i in range(len(samples)):
        bucket = "%s - %s" % (i*bucket_size, (i+1)*bucket_size)
        sample_array.append({'value': samples[i], 'name': bucket, 'index': i})
        data["correct_answers"]["input%s" % (i)] = samples[i]

    data["params"]["samples"] = sample_array
##    data["params"]["sample0"] = samples[0]
##    data["params"]["sample1"] = samples[1]

    ## temporary code to see what is going on in the 'data' dictionary
    data["params"]["data"] = json.dumps(data)

## This causes an error
##    print(json.dumps(data))

    return data


## temporary hack to show that we can dump the 'data' dictionary after student submission.
## def grade(data):
##     data["score"] = 1
## 
##     data["feedback"]["data"] = json.dumps(data)
## 
##     return data
