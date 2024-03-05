#reading and writing files 
"""
modes available
create mode = x
read mode = r
write mode = w
append mode = a
"""

#creation of files
try:
    open("records.txt", "x")
except FileExistsError as e:
    print(f"Err {e}")
#generates exception of the file is already available
    
#writing to the file 
f = open("records.txt", "w")
f.write("I have been writtent from python!")
f.write("End of writing")
#write lines
f.writelines("\nI have been writtent from python!\nEnd of writing")
f.close()

#reading from a file 
f = open("records.txt", "r")
contents = f.read()
print(contents)
f.close()

#appending data
nums = [12,3,4,5,6,7]
f = open("records.txt", "a")
f.write(f"\n{nums}")
f.close()