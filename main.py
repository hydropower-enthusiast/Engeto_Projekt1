"""
projekt_1.py: první­ projekt do Engeto Online Python Akademie

author: Přemysl Harazin
email: harazinpremysl@gmail.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

USERLIST=["bob","ann","mike","liz"]
USERPASSWORDS=["123","pass123","password123","pass123"]

from sys import exit

username=input("username: ")
password=input("password: ")

if username in USERLIST:
    userlist_id=USERLIST.index(username)
    
    if password==USERPASSWORDS[userlist_id]:
        print("Welcome to the app, ",username)
        print("We have ",len(TEXTS)," texts to be analyzed.")
        print("Enter a number between 1 and ", len(TEXTS), "to select:" )
        selected_text=input("")
        if selected_text=="1" or selected_text=="2" or selected_text=="3":
            selected_text=int(selected_text)-1
        else:
            print("Wrong Input, terminating the program..")
            exit()
            
    else:
        print("unregistered user, terminating the program..")
        exit()

else:
    print("unregistered user, terminating the program..")
    exit()


second_empty_list=TEXTS[selected_text].split()

# Odstraneni carky, tecky a noveho paragrafu z textu
helper_list2=second_empty_list[:]
second_empty_list=[]
for xx in helper_list2:
    second_empty_list.append(xx.removesuffix('\n'))

helper_list2=second_empty_list[:]
second_empty_list=[]
for xx in helper_list2:
    second_empty_list.append(xx.removesuffix(','))
    
helper_list2=second_empty_list[:]
second_empty_list=[]
for xx in helper_list2:
    second_empty_list.append(xx.removesuffix('.'))    
    
    
counter_capital_firstletters=0     
counter_capital_allletters=0   
counter_small_allletters=0
counter_amount_of_numbers=0
counter_sum_of_numbers=0

for c in range(0,len(second_empty_list)):
    # Hledani velkych prvnich pismen
    if second_empty_list[c][0].istitle():
        counter_capital_firstletters=counter_capital_firstletters+1
    
    # Hledani slov se samymi velkymi pismeny
    if second_empty_list[c].isupper():
        counter_capital_allletters=counter_capital_allletters+1
    
    # Hledani slov se samymi malymi pismeny
    if second_empty_list[c].islower():
        counter_small_allletters=counter_small_allletters+1

    # Hledani moznych cisel a jejich nasledny soucet
    try:
        float(second_empty_list[c])
        counter_amount_of_numbers=counter_amount_of_numbers+1
        counter_sum_of_numbers=counter_sum_of_numbers+int(second_empty_list[c])
    except ValueError:
        pass


print("There is/are ",len(second_empty_list)," word(s) in the selected text.")        
print("There is/are ",counter_capital_firstletters," titlecase word(s).")
print("There is/are ",counter_capital_allletters," uppercase word(s).")
print("There is/are ",counter_small_allletters," lowercase word(s).")
print("There is/are ",counter_amount_of_numbers," numeric string(s).")
print("The sum of all the numbers is ",counter_sum_of_numbers)


# Vypocet cetnosti ruznych delek slov v textu
max_length_of_string=max(len(x) for x in second_empty_list)
vysledne_delky=[]

for k in range(1,max_length_of_string+1):
    counter=0
    for each in second_empty_list:
        if len(each)==k:
            counter=counter+1
    vysledne_delky.append(counter)

print("------------------------------------------------------------")
print("LEN | Occurences | Nr.")
print("------------------------------------------------------------")

for k in range(0,max_length_of_string):
    print(f"{k+1:>4}|{'*'*vysledne_delky[k]:>0}|{vysledne_delky[k]:>1}") 
    #striska/zobak znamena zarovnani, cislo znaci pocet odsazovacich znaku





























