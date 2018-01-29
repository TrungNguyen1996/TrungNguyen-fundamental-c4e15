from random import randint

# x = randint(0, 100)
# print("A ramdom (0 - 100)", x)

from random import randrange

mood = randrange(0,100)
sad = ''' :/ :/ :/ :/ :/ '''
norm = """( :| :| :| :| )"""
happy = ''' :* :* :* :* '''
print(mood)
if mood<30:
    print (sad)
elif mood<60:
    print (norm)
else:
    print (happy)
