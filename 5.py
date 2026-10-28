'''
PART B - FUNCTIONS (about 40 min total)
 
3. Your first functions  (~10 min)
 
A function packages up code so you can reuse it:
 
    def double(n):
        return n * 2
 
    double(5)  ->  10
 
a) Write is_even(n) that returns True if n is even, False otherwise.
   Hint: n % 2 gives the remainder after dividing by 2.
       is_even(4)  ->  True
       is_even(9)  ->  False
       is_even(0)  ->  True
 
b) Write power(base, exp) that returns base raised to exp.
   If exp is not provided, it defaults to 2.
       power(4)     ->  16
       power(2, 5)  ->  32
 
c) Write sum_of_squares(a, b) that returns a^2 + b^2.
   Use your power() function. Don't multiply directly!
       sum_of_squares(3, 4)  ->  25   # 9 + 16
'''