import os
import shutil

# Create a new directory
os.mkdir("mydir")

# Create a new file in the directory
with open("mydir/myfile.txt", "w") as f:
    f.write("Hello, world!")

# Read the contents of the file
with open("mydir/myfile.txt", "r") as f:
    print(f.read())  # Hello, world!

# Update the contents of the file
with open("mydir/myfile.txt", "w") as f:
    f.write("Goodbye, world!")

# Read the contents of the file again
with open("mydir/myfile.txt", "r") as f:
    print(f.read())  # Goodbye, world!

# Delete the file
os.remove("mydir/myfile.txt")

# Delete the directory
shutil.rmtree("mydir")
