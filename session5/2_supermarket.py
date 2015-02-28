'''

Un dia en el supermercado

'''

First, make a list called groceries with the values "banana","orange", and "apple".

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!


def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
n = [1, 2, 5, 10, 13]
print sum(n)

In the above example, we first define a function called sum with an argument numbers.
We initialize the variable total that we will use as our running sum.
For each number in the list, we add that number to the running sum total.
At the end of the function, we return the running sum.
After the function, we create, n, a list of numbers.
Finally, we call the sum(numbers) function with the variable n and print the result.

Define a function compute_bill that takes one argument food as input.
In the function, create a variable total with an initial value of zero.
For each item in the food list, add the price of that item to total.
Finally, return the total.
Ignore whether or not the item you're billing for is in stock.

Note that your function should work for any food list.

# STOCKING OUT

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!

Now you need your compute_bill function to take the stock/inventory of a particular item into account when computing the cost.

Ultimately, if an item isn't in stock, then it shouldn't be included in the total. You can't buy or sell what you don't have!

Make the following changes to your compute_bill function:

While you loop through each item of food, only add the price of the item to total if the item's stock count is greater than zero.
If the item is in stock and after you add the price to the total, subtract one from the item's stock count.
?


shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!

Perfect! You've done a great job with lists and dictionaries in this project. You've practiced:

Using for loops with lists and dictionaries
Writing functions with loops, lists, and dictionaries
Updating data in response to changes in the environment (for instance, decreasing the number of bananas in stock by 1 when you sell one).
Thanks for shopping at the Codecademy supermarket!