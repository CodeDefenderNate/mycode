# Create list one.

wordbank= ["indentation", "spaces"] 


# Create list two.

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']


# Add a line of code that appends the integer 4 to the list wordbank.

wordbank.append(4)

# Include an input asking for a number between 0 and 20. Save this as the variable num.

num= int(input("Choose a number between 0 and 20: "))

# Use the integer num to slice one of the elements from the list tlgstudents. Save the name you return as the variable student_name.

student_name= tlgstudents[num]

# Using elements from the tlgstudents list and the student_name string, print this output.
# <student_name> always uses <4> <spaces> to indent.

print(student_name +" always uses " + str(wordbank[2]) + " " + wordbank[1] + " to indent. ")
