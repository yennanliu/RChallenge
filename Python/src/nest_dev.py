import argparse
import json
import sys

def parse_args():
    pass 

def read_stdin_input():
    # load input from stdin
    input_data = ''
    for line in sys.stdin.readlines():
        input_data += line 
    # transform string to json for following process 
    return json.loads(input_data)


def read_file_input():
    pass

def append_not_listed(nlevels, data):
    ''' Returns a list of dicts of not considered keys in nlevels '''

    not_listed = []
    for key in data:
        if key not in nlevels:
            not_listed.append({key: data[key]})

    return not_listed

def process_for_output(input_data, json_keys):
    """
    parse CLI args, transform input data to json output  
    """
    output = {}
    tmp = output
    # main algorithm building the final data structure 
    for data in input_data:
        for i, key in enumerate(json_keys):
            if i < len(json_keys) -1:
                if data[key] not in tmp:
                    tmp[data[key]] = {}
                tmp = tmp[data[key]]
            else:
                tmp[data[key]] = append_not_listed(json_keys, data)
        tmp = output
    return output

if __name__ == '__main__':
    json_data = read_stdin_input()
    #print (json_data)
    json_keys = ['country' ,'city', 'currency']
    output = process_for_output(json_data, json_keys)
    print (json.dumps(output, indent=2))
