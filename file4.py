#strings 
msg = "Hello David, good moring! "

#string indexing and slicing! indexing starts at 0
print(msg[0])#gets the first character from msg string
print(msg[0:10])#prints from index 0 to index 10
print(msg[:])#prints the entire msg string
print(msg[::])#print from start to the end
print(msg[::2])#specifying a step

#negative inexing is allowed
print(msg[-8:-1])
print(msg[::-1])#reverse the string (more of a mirror)

#string methods - aid in string manipulation
print(msg.upper())#returns msg in capital letters
print(msg.lower())#returns msg in small letters
print(msg.capitalize())#returns msg in sentence case
print(msg.swapcase())#reverses case for each character
print(msg.title())#makes start of each word character in msg upper
print(len(msg))#returns the length of the string
print(msg.count('David'))#returns no of times David appears 
print(msg.replace("David", "Ivan"))
print(msg.split())#splits the msg, returns a string
#specify the point for splitting
print(msg.split(" "))#split at empty spaces
print(msg.strip())#removes whitespace from the msg string
#strip() can be lstrip() or a rstrip()
print(msg.find("David"))#returns the index where David starts
print(msg.rfind("David"))#returns the last occurance of David
print("David" in msg)#Checks whether David is part of mdg str
print(msg.center(30, "*"))
print(msg.isalnum())
print(msg[2].isalpha())
print(msg[0].isdecimal())
print(msg[0].isdigit())
print(msg.isnumeric())
print(msg.startswith("Hello"))
print(msg.endswith("Hello"))

