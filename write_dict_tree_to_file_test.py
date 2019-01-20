from json import load
from write_dict_tree_to_file import write_dict_tree_to_file

infile = 'write_dict_tree_to_file_test_data.json'
outfile = 'write_dict_tree_to_file_output.txt'

if __name__ == "__main__":
    with open(infile,'r') as f:
        tags_dict = load(f)
    print(f'.../{infile} read')

    with open(outfile,'w') as f:
        f.write('***keys only***')
        write_dict_tree_to_file(f, tags_dict, False)
        f.write('\n\n***keys and values***')
        write_dict_tree_to_file(f, tags_dict)
    print(f'.../{outfile} written')
