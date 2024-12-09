#sometimes we code and make mistakes with our data types. 
#let's try doing the concatenation below.
num_char = len(input('waht is your name? '))
# print('your name has '+ num_char +' characters')
#we have an error above because we're trying to concatennate a string and an integer wc is imposible unless we convert it to one data type. Let's see the solution below.
new_num_char = str(num_char)
print('your name has '+ new_num_char +' characters')

# we can also convert to float, bool, int
