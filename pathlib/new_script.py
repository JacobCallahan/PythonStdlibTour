from pathlib import Path

# Create a new directory
my_file = Path("mydir/myfile.txt")
my_file.parent.mkdir()

# Create a new file in the directory
my_file.write_text("Hello, world!")

# Read the contents of the file
print(my_file.read_text())  # Hello, world!

# Update the contents of the file
my_file.write_text("Goodbye, world!")

# Read the contents of the file again
print(my_file.read_text())  # Goodbye, world!

# Delete the file
my_file.unlink()

# Delete the directory
my_file.parent.rmdir()
