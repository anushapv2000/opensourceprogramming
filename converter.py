import ast
import sys
import yaml
import json 
import os
import jsn
def convert_file(filepath1,filepath2):
  k=filepath1.split('.')
  l=filepath2.split('.')
  if os.path.exists(filepath1):
     with open(filepath1,'r') as file:   
        if  (k[-1]=='yml' or  k[-1]=='yaml') and (l[-1]=='json' or l[-1]=='jsn'): 
            
          #yaml_to_dict=yaml.load(file,Loader=yaml.FullLoader)
          yaml_load=yaml.safe_load(file)
          with open(filepath2,"w") as json_doc:
            json.dump(yaml_load,json_doc,indent=2)
        elif (k[-1]=='json' or k[-1]=='jsn') and (l[-1]=='yaml' or l[-1]=='yml'):
          json_load=json.load(file)
          with open(filepath2,"w") as yaml_doc:
            yaml.dump(json_load,yaml_doc,default_flow_style=False,sort_keys=False)
        else:
            print("invalid file format")
  else:
      return 0

def main():
    if len(sys.argv) == 3:
       filepath1 = sys.argv[1]
       filepath2 = sys.argv[2]
       value=convert_file(filepath1,filepath2)
       if value == 0:
         print("File not found")
    else:
        print("File not Mentioned")
       
if __name__ == "__main__":
    main()
