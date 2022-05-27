from sorter_api import Sorter
import sys

sort_type = sys.argv[1]
sort_order = sys.argv[2]
filename = sys.argv[3]
output_filename = sys.argv[4]

if sort_type == "lex":
    sort_type = "lexicographically"

# Write your code here
sorter_class_instance = Sorter(sort_type, sort_order)

f = open(filename, 'r')
f_contents = f.readlines()

foutput = open(output_filename, 'w')

f_sorted = sorter_class_instance.sort_strings(f_contents)
f_sorted_str = ''.join(f_sorted)
foutput.write(f_sorted_str)

f.close()
foutput.close()


#sorter_class_instance = Sorter(sort_type, sort_order)

#with open(filename, 'r') as input :
#    with open(output_filename, 'w') as output:
#        f_contents = input.read()
#        f_contents_sorted = sorter_class_instance.sort_strings(f_contents)
#       output.write(f_contents_sorted)