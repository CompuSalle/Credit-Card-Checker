# @Copyright
# Created by :
# Waseem Adel Alaa-Iddin
# Can be used in your project. A name maintaining will be nice.



#A function that verifies that the user input is 16 is only numbers
def takingFromUser():
    User_input=''
    while True:
        try:
            User_input = input('[+] Enter (16 digit) credit card number : ')
            if not (len(User_input) == 16) or not type(int(User_input) == int) :
                #if the length is not = 16 and the input is not ONLY numbers ... call the 'Exception' 
                raise Exception
        except Exception:  
            #if any error occurred
            print('\n[!] An error occurred, Please recheck the inputted numbers, and be aware of any characters or spaces.')
            #redo
            continue

        #if success stop
        else:
            break
    return User_input


#A function has been created to ask the user to do again when done or stop
def restart():
    return input('\n[?] Again? (y/N) : ').lower()[0] == 'y'


#Function to evaluate whether its a valid credit card or not
def CreditChecker(the_user_input):

    #add the card number to a list 
    has_been_listed=[]

    #for loop to append and add a single item to from variable 'card' to 'has_been_listed'
    for card in the_user_input:
        has_been_listed.append(int(card))

    for card in range(0,len(the_user_input),2): #range of (start at 0, stops and the_user_input enterd length which is 16 , steps to take which is 2) so (2,16,2)

        #A set of math equations using the Luhn Algorithm (Mod 10 Check) to check the card validation
        has_been_listed[card] = has_been_listed[card]*2 
        if has_been_listed[card] >= 10:
            has_been_listed[card] = has_been_listed[card]//10 + has_been_listed[card]%10

    #finally, if the remainder is = 0 then its valid else it's not valid
    if sum(has_been_listed)%10 == 0:
        print('\n[+] This a valid credit card\n') 

    else:
        print('\n[!] This is not valid credit card\n')

#Main function to call as program starts 
def mainFunction():
    try:
        while True:
            #Take user input as start from this function 'takingFromUser()'
            User_input = takingFromUser()
            #then start this function when done 'CreditChecker'
            CreditChecker(User_input)
            #if user dont want to restart, stop and exit.
            if not restart():
                break
    except KeyboardInterrupt:
        print('\n[!] Keyboard Interrupt')
        

#start 'mainfunction' function
mainFunction()