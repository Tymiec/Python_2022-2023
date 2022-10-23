# Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.
 
# initializing string 
test_string = "Geeksforgeeks is best Computer Science Portal"
 
# printing original string
print ("The original string is : " +  test_string)
 
# using split()
# to extract words from string
res = test_string.split()
 
# printing result
print ("The list of words is : " +  str(res))