#strings

message = """Bob's world 

is cool""" # Three double quotes give you the ability to skip lines

print(message)

message2 ="Bob's world is cool"

print(message2)

#Advanced concepts - Strings

message3 = "Hello World"

print(message3[0]) # []-Sends back the location of the postion entered 
print(message3[1])
print(message3[3])
print(message3[-1])

print(len(message3)) # len-Counts the numder of whitespaces

message4 = " Hello, World "

print(message4.strip()) # .strip()-Removes leading and trailling whitespace
print(message4.lower()) # Converts all characters to lowercase
print(message4.split()) # Splits the string into a little list based on the comma
print(message4.upper()) # Converts all characters to uppercase

text = "apple orange apple banana apple cherry"
new_text = text.replace("apple", "grape")
print(new_text)
# Output: grape orange grape banana grape cherry

text = "one two one three one"
new_text = text.replace("one", "four", 2)
print(new_text)
# Output: four two four three one

word = "hello"
new_word = word.replace("l", "x")
print(new_word)
# Output: hexxo