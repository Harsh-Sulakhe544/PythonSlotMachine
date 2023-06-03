# remember if we bet on 1 line -> first line
# if we bet on line 2 => top 2 lines 
# if 3 => then all 3 lines 

import random  # we need to generate the random values for SLOT MACHINE 
MAX_LINES = 3   #( we have only 3 lines to bet for  )
MAX_BET=100  # max bet for each line
MIN_BET=1  # min bet for each line 
 
ROWS=3   # if we gues 3x3 lines correct we win the game : 
COLS=3
print("\n\n ***************************************WELCOME TO CASINO*************************************** \n\n")
print("***************************************WELCOME TO THE SLOT MACHINE************************ : \n\n")

print("WHAT'S THIS MACHINE ?  \n  RULES TO PLAY THE GAME  : ")
print("1.You have to Select the any Number of lines from line 1 to line 3 \n:")
print("2. If You Select 2 lines ,  it will be counted form  line 1 to line 2 \n:")
print("3. If You Select 3 lines ,  it will be counted form  line 1 to line 3 (all lines) \n:")
print("4. You cannot just Select Any lines ,  Randomly like line 1 and line 3 \n:")
print("5. Initially You Have to Provide the Balance to Play The Game : ")
print("6. TO PLAY THIS GAME , YOU NEED TO GUESS ON ELEMENTS ON EACH ROW SHOWN ON SLOT-MACHINE \n, IF THEY ARE SIMILAR WITH OTHER ELEMNTS ON SAME ROW \n ") 
print("LIKE A|A|A  OR B|B|B  OR C|C|C ON YOUR SELECTED ROW \ ROWS \n , YOU WON! OR ELSE YOU LOSE. ")
print("7. For Each line , You can Bit on your Desired Money \n:")
print("8. If You Win , You get The Calculated Amount And Your Balance Will be Increased ")
print("9. If You Loose , You will Lose your own Amount From balance ")
print("10. YOU CAN PRESS Q ATLEAST AFTER ONE BET TO QUIT ")


print("\n\n")
# check the symbols in each column  as you want we use ABCD  

# these are the content inside SLOT MCHINE
symbol_count= {
    "A" : 2,  # in total we can choose from only out of these (2+4+6+8  => 20) 
    "B" : 4,
    "C" : 6,
    "D" : 8
}

# now particularly look only through those rows that the user bet on => inside the function check_winnings() with the help of symbol_value
symbol_value= {
    "A" : 5,  # in total we can choose from only out of these (2+4+6+8  => 20) 
    "B" : 4,
    "C" : 3,
    "D" : 2
}
# to check whether we won or not : (have a check on balance )  and ( win == A|A|A or B|B|B or C|C|C)
def check_winnings(columns,lines,bet,values) :
    
    winnings=0 # you have not won initially 
    
    winnings_lines=[]  # to check on which of the lines user has won 
    
    # we just need to check the rows that user bet on 
    for line in range(lines):  # if user give the input 2 => check the line 0 and line 1
        
        #so now we need to check each row with each individual value 
        # just check the o th row 0 th column make sure that other columns in row are same 
        #so get the o th row 0 th column
        
        symbol = columns[0][line]
        # now loop all of the columns in that line 
        for column in columns: # we go to each column 
            symbol_to_check=column[line] #check the 0th row 1st element with 2nd element in the same row 
            
            if symbol !=symbol_to_check:
                break
        # if break  => then check on the enxt line 
        # if not break => user won => all symbols are same  => go to else part then (cuz for successfully completed all iterations)
        
        #this else below executes only if for has successfully completed all iterations : 
        # (here no break should take place in if loop then we can go to else part )
        else :     
            winnings +=values[symbol] * bet
            # the bet above is on each line => so user can win the bet on one line and lose on another 
            winnings_lines.append(line + 1) #=>cuz line starts from 0     
            
    return winnings , winnings_lines        
    

# now we want to check the o/p of the SLOT MACHINE
def get_slot_machine_spin(rows , cols , symbols ):
    
    # we need to pick randomly no of rows inside each column ( 3 rows => go inside 3 random symbols)
    # for each colum in each row we want to randomly generate the symbols 
    
    # pick a empty list 
    
    all_symbols=[]
    
    # now we will add the symbols to the list : 
    
    # iterate through a dictionary 
    for symbol,symbol_count in symbols.items(): #(items()  => gives both keys and values associated with dictionary symbols )
        # initially (symbol is A and symbol_count is 2 )
        
        for _ in range(symbol_count) :   # ( _  is anonymous variable in python )
            # since count for A => 2 , we are adding A in 2 times in to list all_symbols
            all_symbols.append(symbol)
            
    # what symbol we should generate on each column based on the frequency of symbol_count 
    # we use for loop for the columns :
    
    # create a nested lists columns[]: where each of the list can represent the values in our column  (we are not storing the rows )
    
    columns=[]  # below code will generate logic in the way => this is actually columns[[],[],[],....]
    
    # now we need to generate the random values for each of the column :  the no of rows we have that many cols we need to generate:
    # (basically matriix format : )
    
    for _ in range(cols):  # generate a column for every single column that we have  
       
       # below code will generate the random values for each of the columns with respective rows 
       
        column=[] #where each of the list can represent the values in our column
        
        # current_symbol is symbol selected for this value on (particular col and particular row)
        current_symbols=all_symbols[:] # we want a copy (so we perform list slicing , otherwise changes made to either one can affect the the other one) 
        
        for _ in range(rows):
            # now i  need to select certain (some ) values from all_symbols list but we can select only limited : ex we can 
            # select only 2 A's  , we can not go for to select  3rd A 
            
            value=random.choice(current_symbols)
            #so now we will remove in order to generate proper number of A , B , C  , D
            # so we select 1 A and then remove it to reselect it (we need to make a copy of (all_symbols list) => current_symbols )
            current_symbols.remove(value)
            # now add this random generated value to the coilumn 
            column.append(value)
        
        # now we add our each column value to the columns list  
        columns.append(column)    
        
    return columns   
    
# now i want to print the random generated columns value : in a 3x3 MATRIX to the console

def print_slot_machine(columns):
    '''
    JUST AN EXAMPLE 
    [A,B,D]
    [D,D,B]
    [C,B,B]
    SO WE NEED TO GENERATE FROM HORIZONTAL TO VERTICAL LIKE (A,D,C) TO PRINT  THE TRANSPOSE OF A MATRIX (ROW <---> COL)
    BUT I WANT TO PRINT THESE NOW IN 3X3 MATRIX FORM 
    '''
    # we need to loop through row first  : and print the current row (like row 0 then row 1 and next row 2 :)
    
    for row in range(len(columns[0])):  # we need to pass one entire column point to start from the begining index 0 to get transpose
        
        for i,column in enumerate(columns) : # now i am looping through all the items inside the columns list(individual column )
            # print the value that is at the first row of that column (basically 0 for 1st iteration )
            
            # but for the last row i dont want extra ( pipe line operator(|) ) at the end (so that only 2 in between EX: A|B|C)
            #so just enumerate(which gives index ) 
            if i !=len(columns)-1 :  # this will give the last element for each row (for which we dont to print | as shown above )
                print(column[row], end=" | ") # to print the rows on the same line with | in between 2 varaibles  use end=" | " 
                
            else :
                print(column[row],end="")    
        
        print() # to come to the next line after each row    
    
def deposit():
    while True:
        # take the user input untill it's true 
        amount = input("What would you like to deposit ? $ ")
        
        if amount.isdigit():  # check whether the user input is integer or valid or not(-111  is not valid )
            amount = int(amount)
            if amount > 0 :
                break
            else :
                print("Amount must be greater than 0. ")
        
        else :
            print("Please Enter a valid Number :")
            
    return amount


# now we want to bet (how many lines ? and how much amount for each line )  (multiple bet amount by number of lines )
def get_number_of_lines():
    while True:
        lines = input("Enter the number of Lines to bet on (1-" + str(MAX_LINES) + ") ? ")
        
        if lines.isdigit():  # check whether the user input is integer or valid or not(-111  is not valid )
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else :
                print("please Enter a valid number of lines  ")
        
        else :
            print("Please Enter a valid Number :")
            
    return lines

# now amount that the user want to bet on each line
def get_bet():
    while True:
        amount = input("What would you like to bet on each line ? $ ")
        
        if amount.isdigit():  # check whether the user input is integer or valid or not(-111  is not valid )
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else :
                print(f"Amount must be between ${MIN_BET}- ${MAX_BET} ")
        
        else :
            print("Please Enter a valid Number :")
            
    return amount
    
def spin(balance):  # play the game per spin to print the lines on which you won
    lines=get_number_of_lines()
    
    # check whether user has more money to (bet within his limits)
    while True:
        
        bet=get_bet()
        total_bet=bet*lines
        
        if total_bet > balance :
            print(f"You do not have enough money to bet , your current balance is : ${balance} ")
            
        else :
            break    
    print(f"you are betting ${bet} on {lines} lines . total bet is ${total_bet}")
    
    # generate the slot machines
    #here slots=columns
    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    
    # print the slot machine 
    print("\n \n Generated slotting machine will be : \n\n ")
    print_slot_machine(slots) 
    print("\n\n")              
    
    winnings, winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You Won ${winnings}.") 
    print(f"You Won on lines : ", *winning_lines)         
    
    return winnings - total_bet # how much user won or lost from this spin 

def main():
    balance = deposit() 
    while True :
        print(f"Current Balance is ${balance} \n\n")
        print("------------------------------------------------------\n")
        answer=input("Press Enter to Play (q to quit) : ")
        if answer == 'q':
            break
        balance += spin(balance)
        
    print("\n------------------------------------------------------\n")
    print("\n------------------------------------------------------\n")
    
    print(f"\n\n You left with ${balance} \n\n")
    print("------------------------------------------------------\n")
    print("THANKS FOR VISITING THE CASINO , HOPE YOU ENJOYED A LOT \n")
    print("DO VISIT AGAIN , TO HAVE SOME MORE ENTERTAINMENT \n\n")
    print("------------------------------------------------------\n")
         

main()