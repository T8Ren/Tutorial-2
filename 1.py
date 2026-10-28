'''
String indexing and slicing
 
Each letter in a string has a position (index), starting at 0:
 
    s = "foobar"
         012345
 
    s[0]    ->  'f'       (first letter)
    s[-1]   ->  'r'       (last letter)
    len(s)  ->  6         (number of letters)
    s[2:5]  ->  'oba'     (from index 2 up to, but NOT including, 5)
    s[::2]  ->  'foa'     (every second letter)
 
Using  s = "Hello world!" , print:
    1. the first letter                  ->  H
    2. the last letter                   ->  !
    3. the length                        ->  12
    4. the first 6 letters               ->  Hello 
    5. every second letter               ->  el o
'''
 
s = "Hello world!"