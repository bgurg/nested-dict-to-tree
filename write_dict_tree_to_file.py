def write_dict_tree_to_file(f, data, show_values=True, level=0):
  '''
  Recursively steps through a nested dictionary and writes a visual tree representation to a file object
  Inputs: 
    - f = file object being written to
    - data = dictionary data being processed
    - show_values (default is True) = whether to include values or just show keys
    - level (default is 0) used during recursion to indicate nesting level
  Outputs:
    - Writes to the file object provided
    - Nothing returned by the function
  '''
  if type(data) == list:
      for item in data:
          if type(item) in {list, dict}:
              write_dict_tree_to_file(f, item, show_values, level)
          elif show_values:
              f.write('\n' + '   |'*(level-1) + '    ' + '   ' + str(item))

  elif type(data) == dict:
      for k,v in data.items():
          f.write('\n' + '   |'*level + '___' + k)            
          if type(v) in {list, dict}:
              if show_values: 
                  f.write(' : ')
              write_dict_tree_to_file(f, v, show_values, level+1)                
          elif show_values:
                  f.write(' : ' + str(v)) 
            
if __name__ == "__main__":
  print('Function: write_dict_tree_to_file')
