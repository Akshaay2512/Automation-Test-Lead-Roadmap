# Example 1: Write in file

# file = open(r"D:\AK Files\Python Automation JUL 2026\test1.txt", "w")
#
# file.write("1st line \n")
# file.write("2nd line \n")
# file.write("3rd line \n")
# file.write("4th line \n")
# file.write("5th line \n")
# file.close()


# Example 2: Read the file
file = open(r"D:\AK Files\Python Automation JUL 2026\test1.txt", "r")
# print(file.read()) # all content
print(file.readline()) # only first line
file.close()


# Example 3: Add new line in existing doc
file = open(r"D:\AK Files\Python Automation JUL 2026\test1.txt", 'a')
file.write("Next line \n")
file.close()