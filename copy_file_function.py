def copy_file(filename, new_filename):
    og_file = open(filename)
    copied_text = og_file.read()
    og_file.close()

    new_file = open(new_filename, 'w')
    new_file.write(copied_text)
    new_file.close()

input_file = raw_input("Please input the full name of the file you wish to copy: ")
output_file = raw_input("Please input a name for the copy: ")

copy_file(input_file, output_file)

checking = open(output_file)

print(checking.read())
