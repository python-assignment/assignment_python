'''1.Write a program which can filter even numbers in a list by using filter function. The list is: 
[1,2,3,4,5,6,7,8,9,10] '''

numbers = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]  # given list

def even_numbers(num):  # here i am defining a function to check if a number is even #
    return num % 2 == 0

even_numbers = list(filter(even_numbers,numbers)) # here i am using a filter fuction to get even numbers #

print(even_numbers)

'''Write a program which can map() to make a list whose elements are square of elements in 
[1,2,3,4,5,6,7,8,9,10]'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # here i am defining a list #

square_num = list(map(lambda x: x**2, numbers)) # here i am using map() to apply a lambda function that square each element #

print(square_num)

'''Write a program which can map() and filter() to make a list whose elements are square of even 
number in [1,2,3,4,5,6,7,8,9,10].'''
num = [1,2,3,4,5,6,7,8,9,10]

even_nums = filter(lambda x : x%2 == 0, num)

squared_even_numbers = map(lambda x: x**2, even_nums)

result = list(squared_even_numbers)
print(result)


'''  Write a program which can filter() to make a list whose elements are even number between 1 and 
20 (both included) '''

def is_even(number): # here creating a function to check if a number is even
    return number % 2 == 0

numbers = list(range(1,21)) # here creating a list of numbers from 1 to 20

even_numbers = list(filter(is_even,numbers)) # here using the filter() to get even numbers

print(even_numbers) # here printing the result


''' Write a program which can map() to make a list whose elements are square of numbers between 
1 and 20 (both included).'''

def square(n): # here i am creating a function the square of a no.
    return n*n

numbers = list(range(1,21)) # here creating a list of numbers from 1 to 20

squares = list(map(square, numbers)) # here map() to apply the square function to each element in the list

print(squares) # printing the result list of square

'Define a class named American and its subclass NewYorker.'

class American:
    def __init__(self):
        print("kanishk singh parihar")

class NewYorker(American):
    def __init__(self):
        super().__init__()
        print("i am in training")   

c1=American()
c2=NewYorker()             


'''Define a class named Rectangle which can be constructed by a length and width. The Rectangle 
class has a method which can compute the area.'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

rect = Rectangle(10, 5)
print(rect.compute_area())    

'''Define a class named Rectangle which can be constructed by a length and width. The Rectangle 
class has a method which can compute the area.'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

rect = Rectangle(10, 5)
print(rect.compute_area())    

'Write a function takes a two-word string and returns True if both words begin with same letter'
def str_same(str):

    word_1 , word_2 = str.split()

    return word_1[0].lower() == word_2[0].lower() 

result=str_same("kanishk kannu")
print(result)   


'''Write a function that capitalizes the first and fourth letters of a name'''

def cap_1st_letter_and_4th(str1):
     
     if len(str1) < 4:
          return str1.capitalize()
    
     return str1[0].upper() + str1[1:3] + str1[3].upper() + str1[4:]

name = cap_1st_letter_and_4th("kanishk")
print(name)



