# read mode
file = open('notes.txt', 'r')
oneLine = file.readline()

content = file.read()

print(content)

print("one line" , oneLine)


#append mode
file = open('notes.txt', 'a')

file.write("\nLearning File Handling")

file.close()


#with statement handles closing the file automatically
with open('notes.txt', 'r') as file:
    content = file.read()
    print(content)



# Pathlib module is used to handle file paths in a platform-independent way. It provides an object-oriented interface for working with file system paths.

from pathlib import Path
file_path = Path("files") / "notes.txt"

# Check if the file exists
file_path = Path("notes.txt")

print(file_path.exists())
print(file_path.is_file())
print(file_path.is_dir())


folder = Path("data")

folder.mkdir(exist_ok=True) # This line creates a new directory named "data" if it doesn't already exist. The exist_ok=True parameter prevents an error from being raised if the directory already exists.

file_path = folder / "notes.txt"
file_path.write_text("this is a new file created using pathlib module", encoding="utf-8") # This line creates a new file named "notes.txt" inside the "data" directory and writes the specified text to it. The encoding="utf-8" parameter ensures that the text is written using UTF-8 encoding.

#read file
content = file_path.read_text(encoding="utf-8") # This line reads the content of the "notes.txt" file using UTF-8 encoding and returns it as a string.
print(content)

