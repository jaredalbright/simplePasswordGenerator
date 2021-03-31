import random

class Password:

    def __init__(self,sequence,limit):
        '''
        No return
        initializes variables
        '''
        self.sequence = sequence
        self.limit = limit

    def create_password(self):
        '''
        Returns password
        Opens the text file for the word list and reads as a list.
        Then creates a password at random based on the sequence of data types.
        '''
        #opens words.txt and turns it into a list
        with open('passwordGen/words.txt') as f:
            words = f.read().splitlines()
        dict_length = len(words)
        
        symbols = ['!','@','%','&','*'] #list can be changed, these were used just to test the program
        password = ''

        #this loop iterates through the list of data types the concatenates a random value for each element to the string
        for element in self.sequence:
            if element == "Word":
                key = random.randint(0,dict_length-1) #not sure the -1 was necessary but I believe random int covers [a,b] rather than [a,b-1]
                password += words[key].capitalize()
            elif element == "Number":
                password += str(random.randint(0,9)) #turns the int to a string for the sake of concatenation
            elif element == "Symbol":
                key = random.randint(0,len(symbols) - 1)
                password += str(symbols[key])
        return password       

            

