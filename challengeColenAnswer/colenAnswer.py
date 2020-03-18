from six import iteritems
import sys
from nested_lookup import get_all_keys
import json

with open('c:/Users/liuco/Downloads/source-data2.json') as access_json:
    read_content = json.load(access_json)
    desiredJsonFile = read_content


def getDuplicatesWithCount(listOfElems):
    ''' Get frequency count of duplicate elements in the given list '''
    dictOfElems = dict()
    # Iterate over each element in list
    for elem in listOfElems:
        # If element exists in dict then increment its value else add it in dict
        if elem in dictOfElems:
            dictOfElems[elem] += 1
        else:
            dictOfElems[elem] = 1    
 
    # Filter key-value pairs in dictionary. Keep pairs whose value is greater than 1 i.e. only duplicate elements from list.
    dictOfElems = { key:value for key, value in dictOfElems.items() if value >= 1}
    # Returns a dict of duplicate elements and their frequency counts
    return dictOfElems

def colenFunc(dict):
    allkeys = get_all_keys(dict)
    sorted(allkeys)
    sortdupekeys = getDuplicatesWithCount(allkeys)
    json.dumps(sortdupekeys)
    sys.stdout.write(str(sortdupekeys) + '\n')

colenFunc(desiredJsonFile)



