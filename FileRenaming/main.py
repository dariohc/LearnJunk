import os
current_dir = os.getcwd() + "\source"
print(current_dir)
os.chdir(current_dir)
print(os.getcwd())
my_files = os.listdir(current_dir)
print(my_files)
for file in my_files:
    new_name = str(file) + ".mat"
    os.renames(file, new_name)
    print(new_name)
