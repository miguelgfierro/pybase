# New feature in Python 3.8, assignment expressions (known as the walrus operator)
# Assignment expression are written with a new notation (:=). This operator is often
# called the walrus operator as it resembles the eyes and tusks of a walrus on its side.
#
# Video explanation: https://realpython.com/lessons/assignment-expressions/
# PEP 572 https://www.python.org/dev/peps/pep-0572/

# Assignment expressions allow you to assign and return a value in the same expression.
walrus = True
print(walrus)  # True

# In Python 3.8, we can combine these two expressions. It will assign walrus to True
# and return True
print(walrus := True)  # True

# Another example with a while loop. This program allows you to input a text until you
# input the word quit.
# inputs = list()
# while True:
#     current = input("Write something: ")
#     if current == "quit":
#         break
#     inputs.append(current)

# # With assignment expressions this code can be simplified
# inputs = list()
# while (current := input("Write something: ")) != "quit":
#     inputs.append(current)
