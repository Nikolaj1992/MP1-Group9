import os
import json
import requests
import pprint
import pandas as pd

# Reads from the url and stores the response in a json file
def readAPI(url, params, headers, myfile):  
    list = []
    response = requests.get(url, params=params, headers=headers).json()
    list.append(response)
    
    # save in json file        
    with open(myfile, 'w') as f:
        json.dump(list,f)
    return