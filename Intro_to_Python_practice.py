''' Chapter 2, Task 11, '''

# KG to Pound
#
# pound = int(input('Pounds you want to convert to KG:'))
# kilogram = 2.20 * pound
# print(f'Converted_Kilograms:{kilogram:.2f}.')

'''Chapter 2, Task 12, Surface Area'''

# a = float(input('Side_A:'))
# b = float(input('Side_B:'))
# c = float(input('Side_C:'))
# surface_area = 2*a*b + 2*b*c + 2*c*a
# print(f'The Surface area of the prism is: {surface_area:.2f} cm^3')

'''Chapter 2, Task 13, Plane speed '''

# distance = 395000
# time = 9000
# speed = float(distance/time)
# print(f"{speed:.2f}m/s")

'''Chapter 2, Task 14, Pool flow'''

# l = 12
# w = 7
# d = 2
# volume = l*w*d
# pump = 17 #per hour
# flow = volume // pump
# print(f"The pool will be empty after {flow} hours")

'''Chapter 2, Task 15, Pool flow'''

# celsius = float(input(('Celsius:')))
# fahrenheit = celsius * 1.8 + 32
# print(f'Fahrenheit: {fahrenheit:.2f}')

# '''Chapter 2, Task 16, Seconds per day'''

# days = int(input('Number of days:'))
# hours = 24*days
# minutes = hours*60
# seconds = minutes*60
# print(f'{days} days consist {seconds:.0f} seconds.')

''' A car starts from a stoplight and is traveling  with a velocity  of 60 m/s. Find the acceleration if the car
# used 20 seconds to reach out it's velocity.
# Acceleration = Change of velocity / Time '''
#
# v_start = 0
# v_final = 60
# time = 20
# acc = (v_final - v_start)/time
# print(f'The acceleration of the car is: {acc:.2f}m/s')

""" 
# Write a program to read the Richter magnitute value from the user and display the result for
# the following conditions using if elif else"""
#
# while True:
#     richter = float(input('Richter Magnitute:'))
#     if richter < 1.0:
#         print(f'Too little value')
#     elif 1 <= richter < 2:
#         print(f'Microearthquakes not felt or rarely felt')
#     elif 2 <= richter < 4:
#         print(f'Very rarely causes damage')
#     elif 4 <= richter < 5:
#         print(f'Damage done to weak buildings')
#     elif 5 <= richter < 6:
#         print(f'Cause damage to the poorly constructed building')
#     elif 6 <= richter < 7:
#         print(f'Causes damage to well-built structures')
#     elif 7 <= richter < 8:
#         print(f'Causes damage to most buildings')
#     elif 8 <= richter < 9:
#         print(f'Causes major destruction')
#     else:
#         print(f'Causes unbelievable damage')

''' Write a program; to display Pascal's triangle
Formula: n! / (k!(n-k)!)'''

# import math
# while True:
#     n = abs(int(input('Insert Raw Number:')))
#     k = int(input('Insert Column Number:'))
#     if k not in range(n+1):
#         print('k must be an integer between 0 and n')
#     else:
#         num = math.factorial(n) / (math.factorial(k)*(math.factorial(n-k)))
#         print(f'The answer is: {num:.0f}')


''' Write a program to display the following pattern: 1 22 333 4444 55555 and 1 21 321 4321 54321 using nested loops'''

# for i in range(1,6):
#     print(f'{i}'*i)


# n = int(input("enter number of rows: "))
#
# for i in range(1,n+1):
#     for s in range(i):
#         print(str(i), end='')
#     print()


# n = int(input("enter number of rows: "))
#
# for i in range(1,n+1):
#     for s in range(i):
#         print(str(i), end='')
#         i -= 1
#     print()    # Add for an empty line

# '''Write a program that uses a while loop yo add up all the even numbers between 100 snd 200'''
# sum = 0
# for i in range(100,201):
#     if i%2 == 0:
#         sum += i
# print(sum)

''' Write a program to print the sum of the following series:
a. 1 + 1/2 + 1/3 ... + 1/n
b. 1/1 + 2**2/2 + 3**3/3 ... + n**n/n '''

# n = int(input('Insert a number:'))
# a = 0
# b = 0
# for i in range(1, n+1):
#     a += 1/i
#     b += i**i/i
# print(f'a = {a:.2f}', f'b = {b:.0f}')

''' Write a program using functions to perform the arithmetic operations'''
#
# def add_num(a,b):
#     sum = a + b
#     print(sum)
# num_1 = 5
# num_2 = 6
# add_num(num_1, num_2)

''' Write a program to find the largest of the three numbers using functions'''

# def maxings(a,b,c):
#     print(max(a,b,c))
# maxings(5,9,3)

# def maxings(a,b,c):
#     if a < b < c:
#         print(c)
#     elif a > b > c:
#         print(a)
#     else:
#         print(b)
# maxings(5,9,11)

''' Write a Python program using functions to find the value of nPk (permutaions) and nCk (combinations)'''
# import math
# while True:
#
#     def per_comb(n,k):
#         p = math.factorial(n)/math.factorial(n-k)
#         print(f'Permutations: {p:.0f}')
#         c = p / math.factorial(k)
#         print(f'Combinations: {c:.0f}')
#
#     try:
#         n = int(input('Total number of items:'))
#         k = int(input('Number of items to pick from the total:'))
#
#         per_comb(n,k)
#     except:
#         print('n MUST BE BIGGER THAN k')
#         print('-'*40)

''' Write a program using functions to display Pascal's triangle'''

# import math
# while True:
#     def pascals_triangle(n,k):
#         if k not in range(n+1):
#             print('k must be an integer between 0 and n')
#         else:
#             num = math.factorial(n) / (math.factorial(k)*(math.factorial(n-k)))
#             print(f'The answer is: {num:.0f}')
#
#     try:
#         n = abs(int(input('Insert Raw Number:')))
#         k = int(input('Insert Column Number:'))
#         pascals_triangle(n,k)
#     except ValueError:
#         print('Oops, this is not a number. Try again:')

''' Write a program using functions to print harmonic progression series and its sum till N terms '''


# def harmonic_progression(a,d,n):
#     single_term = 0
#     sum_terms = 0
#     for i in range(1, n+1):
#         single_term = 1/(a+(i-1)*d)
#         sum_terms += single_term
#         print(f'Single terms: {single_term:.10f}')
#     print(f'Sum: {sum_terms:.2f}')
# harmonic_progression(1,2,5)

''' Write a program using functions to do the following tasks:
        a. Convert milliseconds to hours, minutes and seconds
        b. Compute a sales commission, given the sales amount and the commission rate 
        c. Convert Celsius to Fahrenheit
        d. Compute the monthly payment, given the loan amount, number of years and the annual interest rate'''

# def milsec_conv(milliseconds):
#     seconds = milliseconds/1000
#     minutes = seconds/60
#     hours = minutes/60
#     print(f'Seconds:{seconds:.0f}')
#     print(f'Minutes:{minutes:.0f}')
#     print(f'Hours:{hours:.1f}')
# milsec_conv(2134132)

# def sales_com(amt, com_rate):
#     sales_commission = amt*com_rate
#     print(f'Commission: {sales_commission}')
# sales_com(200000, 0.05)

'''Write a function called rotate_word that takes a string and an integer as parameters,
 and that function should return a new string containing the letters from the original string
 "rotated" by the given amount. For example, "cheer" rotated by 7 is "jolly" and "melon" rotated by -10 is "cubed"'''

# while True:
#     def rotate_word(word, rotation_parameter):
#         rotated_word = ""
#         for each_char in word:
#             letter_index = int(alphabet.find(each_char))
#             rotated_word += alphabet[(letter_index + rotation_parameter)]
#         print(rotated_word)
#
#
#     def main():
#         user_string = input('Enter a word for convertion:')
#         param = int(input('Enter a rotation number:'))
#         rotate_word(user_string, param)
#
#     import string
#     alphabet = string.ascii_lowercase*2
#     main()

''' Write a function that takes a string as an argument and displays the letters backward, one per line'''

# def let_backward(word):
#
#     new_word = word[::-1]
#     for char in new_word:
#         print(char)
#
# def main():
#     user_word = input('Enter a word:')
#     let_backward(user_word)
#
# main()

''' Write a program to access the last character of the string with the help of len() function'''

# def last_char(word):
#     word_inserted = len(word) - 1
#     print(f'{word[word_inserted]}')
#
# def main():
#     user_word = input('Enter a word:')
#     last_char(user_word)
#
# main()

''' Ask the user for a string and then for a number. Print out that string. that many times. (For example,
if the string is Python and the number is 3 you should print out PythonPythonPython.)'''

# def multi_word(word,num):
# #     print(f'{word*num}')
# #
# # def main ():
# #     user_word = str(input('Enter a word:'))
# #     user_num = int(input('Enter a number:'))
# #     multi_word(user_word,user_num)
# #
# # main()

''' Write a program that reads the date in the format (dd/mm/yyyy) and replaces the "/" with "-" 
and displays the date in (dd-mm-yyyy) format'''

# import datetime
#
# year = int(input('Enter a year:'))
# month = int(input('Enter a month:'))
# day = int(input('Enter a day:'))
# date_inserted = datetime.date(year, month, day)
# date_inserted = datetime.datetime.strftime(date_inserted, '%d/%m/%Y')
# date_with_slash = str(date_inserted)
# print(f'Before: {date_with_slash}')
# date_with_slash_split = date_with_slash.split("/")
# date_converted = "-".join(date_with_slash_split)
# print(f'After: {date_converted}')

#
 '''Write a function that finds the number of occurrences of a specified character in a string'''
# def check_char(character, word):
#     count = 0
#     for each_letter in word:
#         if each_letter == character:
#             count += 1
#     print(f'Letter "{character}" is contained {count} times in the word "{word}"')
#
#
# def main():
#     user_char_input = input('Enter a character:')
#     user_word_input = input('Enter a word:')
#     check_char(user_char_input, user_word_input)
#
# main()

'''Write a program that parses a binary number to a decimal integer. For example:
11001 (1* 2**4 + 1* 2**3 + 0* 2**2 + 0* 2**1 + 1* 2**0); 110 (2**3 + 2**2 + 0*2**1'''
# while True:
#     def binary_to_decimal(binary_num):
#
#         num_to_list = list(map(int, str(binary_num)))
#         result = 0
#         for i in range(len(num_to_list)):
#             result += num_to_list[i] * 2**((len(num_to_list) - 1) - i)
#         print(f'Binary number {binary_num} converted to decimal is: {result}')
#
#
#     def main():
#         user_input = int(input('Enter a binary number: (only 0s and 1s):'))
#         binary_to_decimal(user_input)
#
#     main()

'''Write a program that accepts a string form the user and display the same string after removing vowels from it'''


# def vowel_removal(string):
# #     new_word = ''
# #     for each_char in string:
# #         if (each_char =='a' or each_char =='e' or each_char =='o' or each_char =='u' or each_char =='i' or each_char =='y'):
# #             continue
# #         else:
# #             new_word += each_char
# #     print(f'Word {string} without vowels is: {new_word}')
# #
# # def main():
# #     user_input = input('Enter a word:')
# #     vowel_removal(user_input)
# #
# # main()

'''Write a function to insert a string in the middle of the string'''

# def mid_str(word, string):
#
#     a = word
#     b = string
#     new_word = a[:int(len(a)/2)] + b + a[int(len(a)/2):]
#     print(new_word)
#
# def main():
#
#     user_input_word = input(('Word:'))
#     user_input_string = input(('String:'))
#     mid_str(user_input_word, user_input_string)
#
# main()

'''Write a program to sort a string lexicographically'''

# def lexi_sort(string):
#     new_string = list('')
#     for i in string:
#         new_string.append(i)
#     print(new_string)
#     new_string.sort()
#     print(new_string)
# def main():
#     user_input = input('Word:')
#     lexi_sort(user_input)
#
# main()

'''Write a program that creates a list of 10 random integers. 
Then create two lists by name odd_list and even_list that have 
all odd and even values of the list respectively'''

# import random
#
# rand_nums = []
#
# def rand_nums_gen():
#
#     for x in range(10):
#         rand_nums.append(random.randint(1,101))
#     print(rand_nums)
#
# def odd_even_lists(r_nums):
#     odd_list = []
#     even_list = []
#     for i in r_nums:
#         if i % 2 == 0:
#             even_list.append(i)
#         else:
#             odd_list.append(i)
#     print(f'Odds: {odd_list}')
#     print(f'Evens: {even_list}')
#
# def main():
#
#     rand_nums_gen()
#     odd_even_lists(rand_nums)
#
# main()

'''Write a program to sort the elements in ascending order using insertion sort'''

# import random
#
# rand_nums = []
#
# def rand_nums_gen():
#
#     for x in range(10):
#         rand_nums.append(random.randint(1,101))
#     print(rand_nums)
#
# def sort_nums(r_nums):
#     for i in range(1, len(rand_nums)):
#         cur_value = rand_nums[i]
#         position = i
#         while position > 0 and rand_nums[position - 1] > cur_value:
#             rand_nums[position] = rand_nums[position-1]
#             position -= 1
#         rand_nums[position] = cur_value
#     print(rand_nums)
# def main():
#     rand_nums_gen()
#     sort_nums(rand_nums)
#
# main()
#

'''Write a Python program to use binary search to find a key element in a list
target for this exercise: 49'''

# import math
#
# rand_nums = [2, 40, 41, 49, 55, 60, 66, 70, 73, 79]
# target_num = 49
#
# def binary_search(arr, tar):
#
#     n = len(arr)
#     left = 0
#     right = n - 1
#     mid = math.floor((left+right)/2)
#     while left < right:
#
#         if arr[mid] < tar:
#             left = mid + 1
#         elif arr[mid] > tar:
#             right = mid - 1
#         return mid
#
#
#
# def main():
#
#     position = binary_search(rand_nums, target_num)
#     print(f'The target number {target_num} is located in position {position}')
#
# main()

'''Make a list of the first eight letters of the alphabet 
then using the slice operation do the following:
a. Print the first three letters of the alphabet
b. Print any three letters from the middle
c. Print the letters from any particular index to the end of the list'''

# import math
# import random
# import operator
# letters = 'a b c d e f g h'.split()
# letters_a = letters[:3]
# print(f'a: {letters_a}')
# mid = math.floor(len(letters)/2)
#
# def rand_calc():
#     ops = {'+':operator.add,
#            '-':operator.sub,
#          }
#     num1 = mid
#     num2 = 3
#     op = random.choice(list(ops.keys()))  #op receives the value of + or -
#     answer = ops.get(op)(num1,num2)     #get(op) becomes either operator.add or operator.sub
#     return answer
# answer = rand_calc()
#
# if answer > mid:
#     letters_b = letters[mid:answer]
# else:
#     letters_b = letters[mid:answer:-1]
# print(f'b: {letters_b}')
# r_index = random.randint(0,(len(letters)-1))
# letters_c = letters[r_index:]
# print(f'c: {letters_c}')
#

'''Write a program to sort the elements in ascending order using selection sort'''


#
#
# def sort_nums_selection(rand_nums):
#     for index in range(len(rand_nums)-1,0,-1):
#         position_max = 0
#         for location in range(1,index+1):
#             if rand_nums[location] > rand_nums[position_max]:
#                 position_max = location
#         temp = rand_nums[index]
#         rand_nums[index] = rand_nums[position_max]
#         rand_nums[position_max] = temp
#     print(rand_nums)
#
#
#
#
# def main():
#     rand_nums = [34, 8, 64, 62, 73, 91, 68, 36, 47, 60]
#     print(rand_nums)
#     sort_nums_selection(rand_nums)
#
#
# main()
