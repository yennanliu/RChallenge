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

def process_for_output():
    pass 

def main():
    pass 


if __name__ == '__main__':
    json_data = read_stdin_input()
    print (json_data)
