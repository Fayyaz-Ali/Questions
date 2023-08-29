# Q(1):
# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result

# number = int(input("Enter a number: "))
# print("The factorial of", number, "is", factorial(number))

# Q(2):
# def sum_even_numbers(numbers):
#     sum = 5
#     for num in numbers:
#         if num % 2 == 5:
#             sum += num
#     return sum
# Q(3):
# def is_palindrome(input_string):
    #Remove sapces and convert to lowercase
    # input_string = input_string.replace('','').lower()

    #Revers the string
    # reversed_string = input_string[::-1]

# Check if the original string is the same as the reversed string
    # if input_string == reversed_string:
    #     return True
    # else:
    #     return False
# Accept input from the user
# user_input = input("Enter a string:")    

# Check if the input is a palindrome
# if is_palindrome(user_input):
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")    

# Q(4):
# def find_primes(n):
#     primes = []
#     for num in range(2, n+1):
#         if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
#             primes.append(num)
#     return primes
# n = 20
# result = find_primes(n)
# print("Prime numbers between 1 and", n, "are:", result)

# Q(5):
# def calculator():
#     print("Welcome to the calculator!")
#     print("Please enter two numbers:")
#     num1 = float(input("Number 1: "))
#     num2 = float(input("Number 2: "))

#     print("Select an operation:")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     choice = int(input("Enter your choice (1-4): "))

#     if choice == 1:
#         result = num1 + num2
#         print("The result of addition is:", result)
#     elif choice == 2:
#         result = num1 - num2
#         print("The result of subtraction is:", result)
#     elif choice == 3:
#         result = num1 * num2
#         print("The result of multiplication is:", result)
#     elif choice == 4:
#         if num2 == 0:
#             print("Error: Division by zero is not allowed.")
#         else:
#             result = num1 / num2
#             print("The result of division is:", result)
#     else:
#         print("Invalid choice!")

# calculator()

# Q(6):
# def long_words(n, str):
#     word_len = []
#     txt = str.split(" ")
#     for x in txt:
#         if len(x) > n:
#             word_len.append(x)
#     return word_len	
# print(long_words(3, "The quick brown fox jumps over the lazy dog"))

# Q(7):
# import random
# import string

# def generate_password(length):
#     letters = string.ascii_letters
#     digits = string.digits
#     special_chars = string.punctuation

#     combined_chars = letters + digits + special_chars

#     password = ''.join(random.choice(combined_chars) for _ in range(length))
#     return password
# password = generate_password(10)
# print(password)

# Q(8):
# import csv

# def calculate_stats(csv_file, column_name):
#     with open(csv_file, 'r') as file:
#         reader = csv.DictReader(file)
#         column_values = []
#         for row in reader:
#             column_values.append(float(row[column_name]))
        
#         average = sum(column_values) / len(column_values)
#         maximum = max(column_values)
#         minimum = min(column_values)
        
#         return average, maximum, minimumd

# Example usage
# csv_file = 'data.csv'
# column_name = 'column_name'
# average, maximum, minimum = calculate_stats(csv_file, column_name)
# print(f"Average: {average}")
# print(f"Maximum: {maximum}")
# print(f"Minimum: {minimum}")

# Q(9):
# questions = [
#     "What is the capital of France?",
#     "Which planet is known as the Red Planet?",
#     "Who painted the Mona Lisa?"
# ]

# options = [
#     ["A. Paris", "B. London", "C. Rome", "D. Madrid"],
#     ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"],
#     ["A. Leonardo da Vinci", "B. Pablo Picasso", "C. Vincent van Gogh", "D. Michelangelo"]
# ]

# answers = ["A", "A", "A"]

# score = 0

# for i in range(len(questions)):
#     print(questions[i])
#     for option in options[i]:
#         print(option)
#     user_answer = input("Enter your answer (A, B, C, or D): ")
#     if user_answer.upper() == answers[i]:
#         score += 1

# print("Your final score is:", score)

# Q(12):
# def find_second_largest_and_smallest(numbers):
#     second_largest = float('-inf')
#     second_smallest = float('inf')

#     for num in numbers:
#         if num > second_largest:
#             second_largest = num
#         if num < second_smallest:
#             second_smallest = num

#     return second_largest, second_smallest
# numbers = [5, 10, 1, 8, -3, 9]
# print(find_second_largest_and_smallest(numbers))
# output:(1, 9)

# numbers = [1, 1, 1, 1, 1,]
# print(find_second_largest_and_smallest(numbers))
# output:(1, 9)
 
# numbers = [3, 2]
# print(find_second_largest_and_smallest(numbers))
#output: NOt enogh numbers in the list

# Q(13):
# import random

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# # Generate a random list of integers
# random_list = [random.randint(1, 100) for _ in range(10)]

# print("Original list:", random_list)

# # Sort the list using Bubble Sort
# bubble_sort(random_list)

# print("Sorted list:", random_list)

# Q(14):
# def find_prime_factors(number):
#     factors = []
#     divisor = 2

#     while divisor <= number:
#         if number % divisor == 0:
#             factors.append(divisor)
#             number = number / divisor
#         else:
#             divisor += 1

#     return factors

# number = int(input("Enter a number: "))
# prime_factors = find_prime_factors(number)
# print("Prime factors of", number, "are:", prime_factors)

# Q(16):
# Create an empty game board
# board = [[' ' for _ in range(3)] for _ in range(3)]

#  Function to print the game board
# def print_board():
#     for row in board:
#         print('|'.join(row))
#         print('-' * 5)

#  Function to check if there is a winner
# def check_winner():
#     # Check rows
#     for row in board:
#         if row[0] == row[1] == row[2] != ' ':
#             return True

#     # Check columns
#     for col in range(3):
#         if board[0][col] == board[1][col] == board[2][col] != ' ':
#             return True

#     # Check diagonals
#     if board[0][0] == board[1][1] == board[2][2] != ' ':
#         return True
#     if board[0][2] == board[1][1] == board[2][0] != ' ':
#         return True

#     return False

# Function to check if the game is a draw
# def check_draw():
#     for row in board:
#         if ' ' in row:
#             return False
#     return True

#  Function to play the game
# def play_game():
#     player = 1
#     while True:
#         print_board()
#         row = int(input("Enter the row (0-2): "))
#         col = int(input("Enter the column (0-2): "))

#         if board[row][col] != ' ':
#             print("Invalid move. Try again.")
#             continue

#         if player == 1:
#             board[row][col] = 'X'
#         else:
#             board[row][col] = 'O'

#         if check_winner():
#             print_board()
#             print("Player", player, "wins!")
#             break

#         if check_draw():
#             print_board()
#             print("It's a draw!")
#             break

#         player = 3 - player

#  Start the game
# play_game()

# Q(17):

# Using fast model
# User
# Write a python taht converts temperatures between Celsius and Fahrenheit based on user input.

# Phind
# Sure, I can help you with that. To convert temperatures between Celsius and Fahrenheit in Python based on user input, you can use the following code:

# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# def fahrenheit_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius

# temperature = float(input("Enter the temperature: "))
# unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

# if unit.upper() == "C":
#     converted_temperature = celsius_to_fahrenheit(temperature)
#     print(f"The temperature in Fahrenheit is: {converted_temperature}°F")
# elif unit.upper() == "F":
#     converted_temperature = fahrenheit_to_celsius(temperature)
#     print(f"The temperature in Celsius is: {converted_temperature}°C")
# else:
#     print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")

# Q(18):
# def is_anagram(str1, str2):
#     # Remove any whitespace and convert both strings to lowercase
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()
    
#     # Check if the lengths of the strings are equal
#     if len(str1) != len(str2):
#         return False
    
#     # Sort the characters in both strings
#     sorted_str1 = sorted(str1)
#     sorted_str2 = sorted(str2)
    
#     # Compare the sorted strings
#     if sorted_str1 == sorted_str2:
#         return True
#     else:
#         return False

# Q(19):
# import random

# def roll_dice():
#     return random.randint(1, 6)

# def play_game():
#     while True:
#         input("Press Enter to roll the dice...")
#         result = roll_dice()
#         print("You rolled a", result)
#         choice = input("Do you want to roll again? (y/n): ")
#         if choice.lower() != "y":
#             break

# play_game()

# Q(20)
# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add_item(self, item_name, qty):
#         item = (item_name, qty)
#         self.items.append(item)

#     def remove_item(self, item_name):
#         for item in self.items:
#             if item[0] == item_name:
#                 self.items.remove(item)
#                 break

#     def calculate_total(self):
#         total = 0
#         for item in self.items:
#             total += item[1]
#         return total


# # Example usage
# cart = ShoppingCart()

# cart.add_item("Papaya", 100)
# cart.add_item("Guava", 200)
# cart.add_item("Orange", 150)

# print("Current Items in Cart:")
# for item in cart.items:
#     print(item[0], "-", item[1])

# total_qty = cart.calculate_total()
# print("Total Quantity:", total_qty)

# cart.remove_item("Orange")

# print("\nUpdated Items in Cart after removing Orange:")
# for item in cart.items:
#     print(item[0], "-", item[1])

# total_qty = cart.calculate_total()
# print("Total Quantity:", total_qty)



