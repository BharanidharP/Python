#Problem: Given a list of numbers, count how many are positive.
#numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number=0

for num in numbers :

    if num >0:
    
        positive_number +=1
        #print(positive_number)

#Problem: Calculate the sum of even numbers up to a given number n.
# sum_even=0
# even_number =[ x % 2== 0  for x in range(10)]
# print(even_number)
        
#Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

table =3
for x in range(1,11):  #range(1,n+1) means it will go upto the 11
    if x == 5:
        continue
    #print(table , 'X', x, '=', table * x)
    print(table * x)

#Problem: Reverse a string using a loop.
username="Bharani"  
reverse_string="" 

for name in username:
    reverse_string=name + reverse_string
    #reverse_string=reverse_string + name  this will get the same i/p

print(reverse_string)

#Problem: Given a string, find the first non-repeated character

input_str="teeterabcab"

for char in input_str:
    if input_str.count(char) == 1:
        print("char is :",char)
        break

#Problem: Compute the factorial of a number using a while loop.
number=5
fact=1
while number >0:
    #   fact=fact * number 
    #   number= number - 1
    fact *= number
    number -= 1

print("Fact is:",fact)

#Recursive 
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

#Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    user_input=int (input("Enter the value b/w 1 and 10\n"))
    if 1 <= user_input <=10:
        print(f"Your have entered {user_input}")
        break
    else:
        print("Wrong number")
        

#Problem: Check if a number is prime.
    
value=5

is_prime=True

if value > 1:
    for i in range(2,value):
        if ( value % i) == 0:
            is_prime=False
            break

print(is_prime)


#Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
items = [ "banana", "orange", "apple", "mango","banana"]

unique_item=set()

for item in items:
    if item in unique_item:
        print("Duplicate:",item)
        break
    unique_item.add(item)


#Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.
import time
#everthing in seconds
wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1, "- wait time", wait_time, )
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
