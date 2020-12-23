
print
# comment line
""" commenting block of code """
== == == == == == == == == == == == == == == == == == == == == ==
Types of Number
== == == == == == == == == == == == == == == == == == == == == ==
int() - whole integers
float() - decimal numbers
complex() - numbers consisting of a real part and imaginary part

Type-cast: converting from one type of number to another


== == == == == == == == == == == == == == == == == == == == == ==
Arithmetic
== == == == == == == == == == == == == == == == == == == == == ==
no spaces between number and operators
ex. print(1+num)


Integers can be super large, but when multipled by float() it will be shown as scientific notation

// - gives the other part of modulo(good for dividing and rounding down, no need to float it down)
% - gives the remainder

print(47//8) == > 5
print(47 % 8) == > 7

== == == == == == == == == == == == == == == == == == == == == ==
String
== == == == == == == == == == == == == == == == == == == == == ==

print(len("Spaghetti")) == > 9

Indexing into a string works -> print(("Spaghetti"[0])) == > "S"
Negative Indexing is allowed


FUNCTIONS

.index() == > returns the first index, if not found, it'll return error

.count() == > count number of times substring appears, returns zero if not found

concatenation
+ is the same as JS
* works with string and number 
print("s"*5)              # => sssss


FORMAT
using f in front of a single quoted string makes the {} inside placeholders for variables
first_name = "Billy"
last_name = "Bob"
print(f'Your name is {first_name} {last_name}')

.split() - splits at space
IN ORDER TO SPLIT EACH INDIVIDUAL CHAR, YOU HAVE TO LOOP
            ==
            OR
            ==
list("string") ==> ['s','t','r','i','n','g']

.join() - is used on the string object and NOT on the array
"--".join(["hello", "world"])
"hello--world"

in JavaScript
(["hello","word"]).join(" ")


Python does not have NaN
Python uses None instead of null

None = indicates a variable that has no value
- None has its own type of object NoneType
my_var = None
print(my_var is None) #=> True

and/or/not
&&/||/!

== == == == == == == == == == == == == == == == == == == == == ==
Short-Circuit
== == == == == == == == == == == == == == == == == == == == == ==
Python will stop processing conditional expressions as soon as it hits a True or False answer

or 
print(skip or slowValidation())
if skip is True, then right side won't be executed to return True
if skip is False, then right side will be executed to return False

and
print(skip and slowValidation())
if skip is True, right side will still need to be executed to return True
if skip is False, right side won't have to be executed to return False

It's better to put the QUICKER boolean on the left side, because of short-circuiting.


is or is not (PREFERRED, it correctly identifies different number types)
== or != 