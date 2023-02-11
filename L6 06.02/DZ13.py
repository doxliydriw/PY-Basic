# "s-H" -> stuvwxyzABCDEFGH
import string
y = string.ascii_letters
x = input('Input two letters separated by dash:')
print(y[(y.find(x[0])):(y.find(x[2])+1)])

