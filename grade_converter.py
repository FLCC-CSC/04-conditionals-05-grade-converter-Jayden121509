# FILE NAME - grade_converter.py

# NAME: Jayden Blair
# DATE: 3/1/26
# BRIEF DESCRIPTION:  Grade converter that takes a grade from the user and converts it to a letter grade based on a grading scale.


# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print("===== Grade Converter =====")
grade = int(input("Enter a numerical grade (1-100): "))
if grade >= 97:
    print("A+")
elif grade >= 93:
    print("A")
elif grade >= 90:
    print("A-")
elif grade >= 87:
    print("B+")
elif grade >= 83:
    print("B")
elif grade >= 80:
    print("B-")
elif grade >= 77:
    print("C+")
elif grade >= 73:
    print("C")
elif grade >= 70:
    print("C-")
elif grade >= 67:
    print("D+")
elif grade >= 65:
    print("D")
else:
    print("F")








########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?

Not to forget to use elif statements when you have more than two options to choose from.




'''
