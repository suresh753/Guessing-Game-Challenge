import random

random_number = random.randint(1,100)
guesses = []
guess = None
while (True):
    guess = int( input( 'Enter your guess' ) )
    if guess == random_number:
        print "You're Correct and number of tries are {}".format(len( guesses ) + 1)
        break
    else:
        if 1 <= guess <= 100 :
            if not guesses:
                if abs(random_number-guess) <= 10:
                    print 'WARM!'
                else:
                    print 'COLD!'
            else:
                if abs(random_number-guess) > abs(random_number-guesses[-1]):
                    print 'COLDER!'
                else:
                    print 'WARMER!'
        else:
            print 'OUT OF BOUNDS'
        guesses.append( guess )
