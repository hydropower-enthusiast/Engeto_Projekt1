"""
projekt_1.py: první­ projekt do Engeto Online Python Akademie

author: Přemysl Harazin
email: harazinpremysl@gmail.com
"""

from sys import exit

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

USERLIST = ["bob", "ann", "mike", "liz"]
USERPASSWORDS = ["123", "pass123", "password123", "pass123"]

username = input("username: ")
password = input("password: ")

# Kontrola, zda jmeno uzivatele z inputu je v listu zavedenych uzivatelu.
if username in USERLIST:
    # Prideleni indexu k uvedenemu uzivateli a kontrola spravneho hesla.
    userlist_id = USERLIST.index(username)
    if password == USERPASSWORDS[userlist_id]:
        print("----------------------------------------")
        print("Welcome to the app,", username)
        print("We have", len(TEXTS), "texts to be analyzed.")
        print("----------------------------------------")
        helper="Enter a number btw. 1 and "+str(len(TEXTS))+" to select: "
        selected_text = input(helper)
        print("----------------------------------------")
        # Kontrola zda input je cislo a zda odpovidajici text je v systemu. 
        if selected_text.isdigit() and 1 <= int(selected_text) <= len(TEXTS):
            selected_text = int(selected_text) - 1
        else:
            print("Wrong Input, terminating the program..")
            exit()            
    else:
        print("unregistered user, terminating the program..")
        exit()
else:
    print("unregistered user, terminating the program..")
    exit()

# Rozdeleni slov z celkoveho textu na jednotlive slova
splitted_words = TEXTS[selected_text].split()

# Odstraneni carky, tecky a noveho paragrafu z textu
cleaned_words = []
for word in splitted_words:
    a = word.removesuffix('\n')
    b = a.removesuffix(',')
    c = b.removesuffix('.')
    cleaned_words.append(c)    

# Boolean je podtypem integeru
# Suma vsech slov s prvnim pismenem velkym 
counter_capital_firstletters = sum(
    counter_capital_firstletters2[0].istitle() 
    for counter_capital_firstletters2 in cleaned_words
    )

# Suma vsech slov se vsemi velkymi pismeny 
counter_capital_allletters = sum(
    counter_capital_allletters2.isupper() 
    for counter_capital_allletters2 in cleaned_words
    )

# Suma vsech slov se vsemi malymi pismeny 
counter_small_allletters = sum(
    counter_small_allletters2.islower() 
    for counter_small_allletters2 in cleaned_words
    )

# Pocet slov v textu ktere jsou cisla
counter_amount_of_numbers = sum(
    counter_amount_of_numbers2.isdigit() 
    for counter_amount_of_numbers2 in cleaned_words
    )

# Suma vsech cisel v textu 
counter_sum_of_numbers = sum(int(digit) 
    for digit in cleaned_words if digit.isdigit()
    )

print("There are", len(cleaned_words), "words in the selected text.")        
print("There are", counter_capital_firstletters, "titlecase words.")
print("There are", counter_capital_allletters, "uppercase words.")
print("There are", counter_small_allletters, "lowercase words.")
print("There are", counter_amount_of_numbers, "numeric strings.")
print("The sum of all the numbers", counter_sum_of_numbers)

# Cyklus prochazi pres list, zjistuje delku kazdeho slova, 
# kontroluje zda se jiz dana delka slova nachazi ve slovniku, 
# pokud ano, prida o jedno vic, pokud jeste ve slovniku neni,prida do slovniku.

counter = {}
for word in cleaned_words:
    n = len(word)
    if n in counter:
        counter[n] += 1
    else:
        counter[n] = 1

print("----------------------------------------")
print("LEN | Occurences | NR.")
print("----------------------------------------")

# Cyklus prochazi pres slovnik a zajistuje vypis jednotlivych hodnot
# delka slova, cetnost vyskytu pomoci grafu a nakonec i ciselny vypis.

end_line = max(counter.values()) + 5
max_length_of_word = max(len(word) for word in cleaned_words)
for k in range(1, max_length_of_word + 1):
    try:
        indentation = end_line - counter.get(k)
        # striska/zobak znamena zarovnani, 
        # indentation znaci pocet odsazovacich znaku
        print(f"{k:>4}|{'*'*counter.get(k):>0}"
              f"{' ':>{indentation}}|{counter.get(k):>0}"
              )
        
    except TypeError:
        indentation = end_line
        print(f"{k:>4}|{'*'*0:>0}{' ':>{indentation}}|{0:>0}")

