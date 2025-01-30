### Day 24 - Files, Directories and Paths
- Day 24 Project - The Mail Merge Challenge

Today's project automates writing personalized invitations including the name of each invited person:
- Given a list of invited names and a sample invitation letter, the program generates a file for each invited person named "letter_for_[name].txt", with the invitation letter. In each invitation, the string "[name]" is substituted by the person's name.


### Day 24 Resources
- [Python File readlines() Method](https://www.w3schools.com/python/ref_file_readlines.asp)
- [Python String strip() Method](https://www.w3schools.com/python/ref_string_strip.asp)
- [Python String replace() Method](https://www.w3schools.com/python/ref_string_replace.asp)



### How to Open, Read and Write to Files:

Open a txt file and print its content:
```
file = open("day24/my_file.txt")
contents = file.read()
print(contents)
file.close()
# Why do we have to close the file?
# It will take up computer resources until it is closed (just like having many tabs open on your web browser).
```
Why do we have to close the file every time? An open file will take up computer resources until it is closed (just like having many tabs open on your web browser).

To only keep the file open while we are using it, we can instead code:
```
with open("day24/my_file.txt") as file:
    contents = file.read()
    print(contents)
```

What if we want to write on the file?
The default mode to open a file is "read only". If we want to write to the file, we need to open it into writable mode "w".
```
with open("day24/my_file.txt", mode="w") as file:
file.write("New text.")
# Anything that was previously written in the file will be substituted by "New text."
```

If, instead of substituting the whole text in a file, we just want to add something, we use the mode "a" to add (append) a text.
```
with open("day24/my_file.txt", mode="a") as file:
file.write("\nNew text.")
```

If you open a file in write mode and the file doesn't currently exist, the file will be created for you.

### Understanding Absolute and Relative File Paths

- An Absolute File Path is the path all the way from the root until the file you want to access.
```
/Work/Project/talk.ppt
```
- A Relative File Path specifies the path starting from the Working Directory.
```
# Starting from the Project folder and accessing a document in the same folder:
./talk.ppt
```
```
# Starting from the Project folder and going back to the Work folder:
../talk.ppt
```