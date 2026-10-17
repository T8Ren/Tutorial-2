'''
Lists (arrays)
 
A list holds many items in square brackets. Indexing works just like strings:
 
    fruits = ["apple", "banana", "cherry", "mango", "orange", "kiwi"]
    fruits[0]    ->  "apple"
    fruits[-1]   ->  "kiwi"
    fruits[1:3]  ->  ["banana", "cherry"]
 
Unlike strings, you CAN change a list:
    fruits[-1] = "potato"
 
Tasks:
    1. Print the first fruit.                 ->  apple
    2. Print the last fruit.                  ->  kiwi
    3. Print fruits[2:4].                     ->  ['cherry', 'mango']
    4. Change the last fruit to "potato" and print the list.
    5. Turn the string "foobar" into a list of letters with list() and print it.
                                              ->  ['f', 'o', 'o', 'b', 'a', 'r']
'''
 
fruits = ["apple", "banana", "cherry", "mango", "orange", "kiwi"]