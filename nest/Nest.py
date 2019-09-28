import argparse
import json
import sys

class Json2NestedJson:
    """
    main class offer json to nested json transformation 
    """
    def read_stdin_input(self):
        """
        load input via stdin
        """
        input_data = ''
        for line in sys.stdin.readlines():
            input_data += line 
        # transform string to json for following process 
        return json.loads(input_data)


    def read_file_input(self, json_file):
        """
        load input via json load 
        """
        with open(json_file) as json_data:
            data = json.load(json_data)
        return data 


    def append_not_listed(self, json_keys, data):
        """
        return list of dicts which are not in the json_keys from CLI args 
        """
        not_listed = []
        for key in data:
            if key not in json_keys:
                not_listed.append({key: data[key]})
        return not_listed

    def process_for_output(self, input_data, json_keys):
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
                    tmp[data[key]] = self.append_not_listed(json_keys, data)
            tmp = output
        return output

    def run(self):
        """
        function parse input json to final nested outout json with the CLI args 
        """
        parser = argparse.ArgumentParser(description='CLI for process json')
        # parse CLI arg : keys levels for final output json  
        parser.add_argument('output_dict_keys', 
            type=str, 
            nargs='+',
            help="""run the script via : \n
                 cat Python/data/input.json  | python Python/src/nest_dev.py <key1> <key2> ... \n
                 e.g. :  cat Python/data/input.json | python Python/src/nest_dev.py country city currency""")
        args = parser.parse_args()
        # load the json data via stdin 
        json_data = self.read_stdin_input()
        # transform json to final output form  
        output = self.process_for_output(json_data, args.output_dict_keys)
        print (json.dumps(output, indent=2)) 
