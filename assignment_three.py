import mysql.connector
from mysql.connector import errorcode
import csv
import os


#Setup for the connectiont to sql
cnx = mysql.connector.connect(
    user = "root",
    password = "root",
    host = "127.0.0.1"
)
cursor = cnx.cursor()
dir_path = os.getcwd()

DB_NAME = "drinking_buddy"

#Create the database.
def create_database(cursor, DB_NAME):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

#Creates table for brewweys
def create_table_brewery(cursor):
    create_brewery = "CREATE TABLE `brewery` ( "\
                     " `Brewery` varchar(40) NOT NULL,"\
                     " `Country` varchar(20) NOT NULL,"\
                     " `Founded` varchar(4) NOT NULL,"\
                     " `Most_selling` varchar(30) NOT NULL,"\
                     " `Founders` varchar(85) NOT NULL,"\
                     "PRIMARY KEY (`Brewery`)"\
                     ") ENGINE = InnoDB"
    
    try:
        print("Creating table brewery")
        cursor.execute(create_brewery)
    except mysql.connector.Error as err:
        if  err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table already exists.")
        else:
            print(err.msg)
    else:
        print("Table was created.")

#Create table for ale.
def create_table_ale(cursor): 
    create_ale = "CREATE TABLE `ale` ( "\
                     " `Beer` varchar(35) NOT NULL,"\
                     " `Type` varchar(25) NOT NULL,"\
                     " `ABV` varchar(4) NOT NULL,"\
                     " `Manufacturers` varchar(60) NOT NULL,"\
                     " `Food` varchar(30) NOT NULL,"\
                     " `Taste` varchar(160) NOT NULL,"\
                     " `Price` varchar(8) NOT NULL,"\
                     " `Volume` varchar(5) NOT NULL,"\
                     " `Untappd_rating` varchar(6) NOT NULL,"\
                     " PRIMARY KEY (`Beer`)"\
                     ") ENGINE = InnoDB"
    
    try:
        print("Creating table ale")
        cursor.execute(create_ale)
    except mysql.connector.Error as err:
        if  err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table already exists.")
        else:
            print(err.msg)
    else:
        print("Table was created.")

#Create table for lager.
def create_table_lager(cursor):
    create_lager = "CREATE TABLE `lager` ( "\
                     " `Beer` varchar(35) NOT NULL,"\
                     " `Type` varchar(25) NOT NULL,"\
                     " `ABV` varchar(4) NOT NULL,"\
                     " `Manufacturers` varchar(60) NOT NULL,"\
                     " `Food` varchar(30) NOT NULL,"\
                     " `Taste` varchar(160) NOT NULL,"\
                     " `Price` varchar(8) NOT NULL,"\
                     " `Volume` varchar(5) NOT NULL,"\
                     " `Untappd_rating` varchar(6) NOT NULL,"\
                     "PRIMARY KEY (`Beer`)"\
                     ") ENGINE = InnoDB"
    
    try:
        print("Creating table lager")
        cursor.execute(create_lager)
    except mysql.connector.Error as err:
        if  err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table already exists.")
        else:
            print(err.msg)
    else:
        print("Table was created.")

#Creates table for Sour
def create_table_sour(cursor):
    create_sour = "CREATE TABLE `sour` ( "\
                     " `Beer` varchar(35) NOT NULL,"\
                     " `Type` varchar(25) NOT NULL,"\
                     " `ABV` varchar(4) NOT NULL,"\
                     " `Manufacturers` varchar(60) NOT NULL,"\
                     " `Food` varchar(30) NOT NULL,"\
                     " `Taste` varchar(160) NOT NULL,"\
                     " `Price` varchar(8) NOT NULL,"\
                     " `Volume` varchar(5) NOT NULL,"\
                     " `Untappd_rating` varchar(6) NOT NULL,"\
                     "PRIMARY KEY (`Beer`)"\
                     ") ENGINE = InnoDB"
    
    try:
        print("Creating table sour")
        cursor.execute(create_sour)
    except mysql.connector.Error as err:
        if  err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table already exists.")
        else:
            print(err.msg)
    else:
        print("Table was created.") 

#Creates table for Stouts
def create_table_stout(cursor):
    create_stout = "CREATE TABLE `stout` ( "\
                     " `Beer` varchar(35) NOT NULL,"\
                     " `Type` varchar(25) NOT NULL,"\
                     " `ABV` varchar(4) NOT NULL,"\
                     " `Manufacturers` varchar(60) NOT NULL,"\
                     " `Food` varchar(30) NOT NULL,"\
                     " `Taste` varchar(260) NOT NULL,"\
                     " `Price` varchar(8) NOT NULL,"\
                     " `Volume` varchar(5) NOT NULL,"\
                     " `Untappd_rating` varchar(6) NOT NULL,"\
                     "PRIMARY KEY (`Beer`)"\
                     ") ENGINE = InnoDB"
    
    try:
        print("Creating table sour")
        cursor.execute(create_stout)
    except mysql.connector.Error as err:
        if  err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table already exists.")
        else:
            print(err.msg)
    else:
        print("Table was created.")

#Creates table for Wheat
def create_table_wheat(cursor):
    create_wheat = "CREATE TABLE `wheat` ( "\
                     " `Beer` varchar(35) NOT NULL,"\
                     " `Type` varchar(25) NOT NULL,"\
                     " `ABV` varchar(4) NOT NULL,"\
                     " `Manufacturers` varchar(60) NOT NULL,"\
                     " `Food` varchar(30) NOT NULL,"\
                     " `Taste` varchar(160) NOT NULL,"\
                     " `Price` varchar(8) NOT NULL,"\
                     " `Volume` varchar(5) NOT NULL,"\
                     " `Untappd_rating` varchar(6) NOT NULL,"\
                     "PRIMARY KEY (`Beer`)"\
                     ") ENGINE = InnoDB"
    
    try:
        print("Creating table wheat")
        cursor.execute(create_wheat)
    except mysql.connector.Error as err:
        if  err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table already exists.")
        else:
            print(err.msg)
    else:
        print("Table was created.") 

#Inserts data into the planets table.
def insert_into_brewery(cursor):
    brewery = dir_path + r'\Brewery.csv' # path to the the csv-file. 
    insert_sql = []
    with open(brewery, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        row_counter = 0
        for row in csv_reader:
            if row_counter == 0: #Skips the first line in the csv-file.
                row_counter += 1
            else:
                values_in_row = (f'("{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}", "{row[4]}");')
                querys = (
                    "INSERT INTO brewery (Brewery, Country, Founded, Most_Selling, Founders)"
                    " VALUES " + values_in_row 
                )
                insert_sql.append(querys)

    for query in insert_sql:
        try:
            # print("SQL query {}".format(query), end="")
            cursor.execute(query)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            cnx.commit()

#Inserts data into the ale table.
def insert_into_ale(cursor):
    ale = dir_path + r'\Ale.csv' 
    insert_sql = []
    line_counter = 0
    with open(ale, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if line_counter == 0: 
                line_counter += 1
            else:
                values_in_row = (f'("{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}", "{row[4]}", "{row[5]}", "{row[6]}", "{row[7]}", "{row[8]}");')
                querys = (
                    "INSERT INTO ale(Beer, Type, ABV, Manufacturers, Food, Taste, Price, Volume, Untappd_rating)"
                    " VALUES " + values_in_row 
                )
                insert_sql.append(querys)

    for query in insert_sql:
        try:
            # print("SQL query {}".format(query), end="")
            cursor.execute(query)

        except mysql.connector.Error as err:
            print(err.msg)
        else:
            cnx.commit()

#Inserts data into the lager table.
def insert_into_lager(cursor):
    ale = dir_path + r'\Lager.csv' 
    insert_sql = []
    line_counter = 0
    with open(ale, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if line_counter == 0: 
                line_counter += 1
            else:
                values_in_row = (f'("{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}", "{row[4]}", "{row[5]}", "{row[6]}", "{row[7]}", "{row[8]}");')
                querys = (
                    "INSERT INTO lager(Beer, Type, ABV, Manufacturers, Food, Taste, Price, Volume, Untappd_rating)"
                    " VALUES " + values_in_row 
                )
                insert_sql.append(querys)

    for query in insert_sql:
        try:
            # print("SQL query {}".format(query), end="")
            cursor.execute(query)

        except mysql.connector.Error as err:
            print(err.msg)
        else:
            cnx.commit()

#Inserts data into the sour table.
def insert_into_sour(cursor):
    ale = dir_path + r'\Sour.csv' 
    insert_sql = []
    line_counter = 0
    with open(ale, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if line_counter == 0: 
                line_counter += 1
            else:
                values_in_row = (f'("{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}", "{row[4]}", "{row[5]}", "{row[6]}", "{row[7]}", "{row[8]}");')
                querys = (
                    "INSERT INTO sour(Beer, Type, ABV, Manufacturers, Food, Taste, Price, Volume, Untappd_rating)"
                    " VALUES " + values_in_row 
                )
                insert_sql.append(querys)

    for query in insert_sql:
        try:
            # print("SQL query {}".format(query), end="")
            cursor.execute(query)

        except mysql.connector.Error as err:
            print(err.msg)
        else:
            cnx.commit()

#Inserts data into the stout table.
def insert_into_stout(cursor):
    ale = dir_path + r'\Stout.csv' 
    insert_sql = []
    line_counter = 0
    with open(ale, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if line_counter == 0: 
                line_counter += 1
            else:
                values_in_row = (f'("{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}", "{row[4]}", "{row[5]}", "{row[6]}", "{row[7]}", "{row[8]}");')
                querys = (
                    "INSERT INTO stout(Beer, Type, ABV, Manufacturers, Food, Taste, Price, Volume, Untappd_rating)"
                    " VALUES " + values_in_row 
                )
                insert_sql.append(querys)

    for query in insert_sql:
        try:
            # print("SQL query {}".format(query), end="")
            cursor.execute(query)

        except mysql.connector.Error as err:
            print(err.msg)
        else:
            cnx.commit()

#Inserts data into the wheat table.
def insert_into_wheat(cursor):
    ale = dir_path + r'\Wheat.csv' 
    insert_sql = []
    line_counter = 0
    with open(ale, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if line_counter == 0: 
                line_counter += 1
            else:
                values_in_row = (f'("{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}", "{row[4]}", "{row[5]}", "{row[6]}", "{row[7]}", "{row[8]}");')
                querys = (
                    "INSERT INTO wheat(Beer, Type, ABV, Manufacturers, Food, Taste, Price, Volume, Untappd_rating)"
                    " VALUES " + values_in_row 
                )
                insert_sql.append(querys)

    for query in insert_sql:
        try:
            # print("SQL query {}".format(query), end="")
            cursor.execute(query)

        except mysql.connector.Error as err:
            print(err.msg)
        else:
            cnx.commit()

#Prints the main menu
def mainmenu():
    print(
        "Main menu\n"
        "----------------------------------------------------------------\n"
        "1. List all breweries\n"
        "2. List all the types of beer.\n"
        "3. List all the beer of certin typ.\n"
        "4. List all the beers.\n"
        "5. Search for beer with higher ABV than given limit.\n"
        "6. What beer(s) does the brewery make?\n"
        "7. Average ABV per type of beer.\n"
        "8. Details about a certin brewery.\n"
        "9. Details about a certin beer.\n"
        "10. Where and who makes a certin beer.\n"
        "Q. Exit program\n"
        "----------------------------------------------------------------\n"
    )

#Creates a view with all the beers and their type  
def view_one():
    cursor.execute(
        "CREATE VIEW all_beers AS "
        "SELECT beer, type "
        "FROM Ale "
        "UNION "
        "SELECT beer, type "
        "FROM Lager "
        "UNION "
        "SELECT beer, type "
        "FROM Sour "
        "UNION "
        "SELECT beer, type "
        "FROM Stout "
        "UNION "
        "SELECT beer, type "
        "FROM Wheat"
    )

#Returns all the brewerys.
def option_one():
    cursor.execute(
        "SELECT brewery " 
        "FROM brewery "
        "ORDER BY brewery"
    )
    countrys = cursor.fetchall()
    row_counter = 0
    for country in countrys:
        for name in country:
            print(name)
        row_counter += 1

    else:
        user_input = input(
            "-----------------------------------------\n"
            "1. Search more about a certain brewery\n"
            "-----------------------------------------\n"
            "Please choose a option or press enter to return to the main menu: "
        )
        if user_input == "1":
            option_eight()
        else:
            pass

#Returns all the types of beers.
def option_two():
    cursor.execute(
        "SELECT type "
        "FROM all_beers "
        "GROUP BY type"
    )
    types = cursor.fetchall()
    for type in types:
        for name in type:
            print(name)

    user_input = input(
        "-----------------------------------------\n"
        "1. Search more about a certain type.\n"
        "-----------------------------------------\n"
        "Please choose a option or press enter to return to the main menu: "
    )
    if user_input == "1":
        option_three()
    else:
        pass

#Return all the beers thats belong with the type input.
def option_three():
    type_input = input("What type would you like to have listed? ")
    cursor.execute(
        "SELECT beer "
        "FROM all_beers "
        f"WHERE type = '{type_input}'"
    )
    beers = cursor.fetchall()
    row_counter = 0
    for beer in beers:
        for name in beer:
            print(name)
            row_counter += 1

    if row_counter == 0:
        print("Sorry, the database doens't have that type.")
        input("Press enter to go back to the main menu: ")

    else:
        user_input = input(
            "-----------------------------------------\n"
            "1. Search more about a certain type.\n"
            "2. Search more about a certain beer.\n"
            "-----------------------------------------\n"
            "Please choose a option or press enter to return to the main menu: "
        )
        if user_input == "1":
            option_three()
        elif user_input == "2":
            option_nine()
        else:
            pass

#Returns all the beers.
def option_four():
    cursor.execute(
        "SELECT beer "
        "FROM all_beers"
    )
    beers = cursor.fetchall()
    for beer in beers:
        for name in beer:
            print(name)

    user_input = input(
        "-----------------------------------------\n"
        "1. Search more about a certain beer\n"
        "-----------------------------------------\n"
        "Please choose a option or press enter to return to the main menu: "
    )
    if user_input == "1":
        option_nine()
    else:
        pass

#Ask for a ABV input then returns all the beers with a higher ABV then the input. 
def option_five():
    ABV_input = input("Enter a ABV limit (0-100): ")
    cursor.execute(
        "SELECT beer, abv "
        "FROM ale "
        f"Where abv > {ABV_input} "
        "UNION "
        "SELECT beer, abv "
        "FROM lager "
        f"Where abv > {ABV_input} "
        "UNION "
        "SELECT beer, abv "
        "FROM sour "
        f"Where abv > {ABV_input} "
        "UNION "
        "SELECT beer, abv "
        "FROM stout "
        f"Where abv > {ABV_input} "
        "UNION "
        "SELECT beer, abv "
        "FROM wheat "
        f"Where abv > {ABV_input} "
    )
    abv_limit = cursor.fetchall()
    row_counter = 0

    for name in abv_limit:
        for abv in name:
            if row_counter == 2: #Linebreak
                print("%") 
                row_counter = 0
            print(f"{abv} ", end="")
            row_counter += 1

    if row_counter == 0:
        print("Sorry, the database doens't have beer over that limit.")
        input("Press enter to go back to the main menu: ")
    else:
        print("%")
        user_input = input(
            "-----------------------------------------\n"
            "1. Search more about a certain beer\n"
            "-----------------------------------------\n"
            "Please choose a option or press enter to return to the main menu: "
        )
        if user_input == "1":
            option_nine()
        else:
            pass

#Ask for a brewery input then return the brewery and all the beer that the brewery makes.
def option_six():
    brewery_input = input("Enter a brewery: ")
    cursor.execute(
        "SELECT beer, type "
        "FROM sour JOIN brewery ON sour.manufacturers = brewery.brewery " 
        f"WHERE brewery.brewery = '{brewery_input}'"
        "UNION "
        "SELECT beer, type "
        "FROM stout JOIN brewery ON stout.manufacturers = brewery.brewery "
        f"WHERE brewery.brewery = '{brewery_input}'"
        "UNION "
        "SELECT beer, type "
        "FROM wheat JOIN brewery ON wheat.manufacturers = brewery.brewery "
        f"WHERE brewery.brewery = '{brewery_input}'"
        "UNION "
        "SELECT beer, type "
        "FROM lager JOIN brewery ON lager.manufacturers = brewery.brewery "
        f"WHERE brewery.brewery = '{brewery_input}'"
        "UNION "
        "SELECT beer, type "
        "FROM ale JOIN brewery ON ale.manufacturers = brewery.brewery "
        f"WHERE brewery.brewery = '{brewery_input}'"
    )
    
    beers = cursor.fetchall()
    row_counter = 0
    number = 1
    for beer in beers:
        row = 0
        for name in beer:
            if row == 0:
                print(f"Beer {number}: {name}", end=" " )
                number += 1
                row += 1
            else:
                print(f"Type: {name}")
            row_counter += 1
                
    if row_counter == 0:
        print("Sorry, the database doens't have that brewery.")
        input("Press enter to go back to the main menu: ")
    else:
        user_input = input(
            "-----------------------------------------\n"
            "1. Search more about a certain beer\n"
            "-----------------------------------------\n"
            "Please choose a option or press enter to return to the main menu: "
        )
        if user_input == "1":
            option_nine()
        else:
            pass

#Returns the average ABV of all the types of beer.
def option_seven():
    cursor.execute(
       "SELECT type, AVG(abv) "
       "FROM sour "
       "GROUP BY type "
       "UNION "
       "SELECT type, AVG(abv) "
       "FROM stout "
       "GROUP BY type "
       "UNION "
       "SELECT type, AVG(abv) "
       "FROM wheat "
       "GROUP BY type "
       "UNION "
       "SELECT type, AVG(abv) "
       "FROM lager "
       "GROUP BY type "
       "UNION "
       "SELECT type, AVG(abv) "
       "FROM ale "
       "GROUP BY type"
   )

    average_abv = cursor.fetchall()
    row_counter = 0
    for type in average_abv:
        for abv in type:
            if row_counter == 2: #Linebreak
                print("%")
                row_counter = 0
            print(f"{abv} ", end="")
            row_counter += 1
    print("%")
    
    user_input = input(
        "-----------------------------------------\n"
        "1. Search more about a certain type.\n"
        "-----------------------------------------\n"
        "Please choose a option or press enter to return to the main menu: "
    )
    if user_input == "1":
        option_three()
    else:
        pass

#Ask for a brewery input and returns the information about the brewery.
def option_eight():
    brewery_input = input("What brewery would you like to know more about? ")
    cursor.execute(
        "SELECT * "
        "FROM brewery "
        f"WHERE brewery = '{brewery_input}'"
    )
    brewery_info = cursor.fetchall()
    column = ["Brewery","Country","Founded","Most selling beer","Founders"]# Brewery table columns. 
    row_counter = 0

    for row in brewery_info: #Prints the column and the propper vaule. 
        for info in row:
            print(f"{column[row_counter]}: {info}")
            row_counter += 1
    
    #If the fetch doesn't get any data the program should act accordingly
    if row_counter == 0:
        print("Sorry, the database doens't have that brewery.")
        input("Press enter to go back to the main menu: ")
    else:
        user_input = input(
            "-----------------------------------------\n"
            "1. Search more about a certain brewery\n"
            "-----------------------------------------\n"
            "Please choose a option or press enter to return to the main menu: "
        )
        if user_input == "1":
            option_eight()
        else:
            pass

#Ask for a beer input and return information about the beer.
def option_nine():

    beer_input = input("What beer would you like to know more about? ")
    cursor.execute(
        "SELECT * "
        "FROM sour "
        f"WHERE beer = '{beer_input}' "
        "UNION "
        "SELECT * "
        "FROM stout "
        f"WHERE beer = '{beer_input}' "
        "UNION "
        "SELECT * "
        "FROM wheat "
        f"WHERE beer = '{beer_input}' "
        "UNION "
        "SELECT * "
        "FROM lager "
        f"WHERE beer = '{beer_input}' "
        "UNION "
        "SELECT * "
        "FROM ale "
        f"WHERE beer = '{beer_input}' "
    )

    beer_info = cursor.fetchall()
    column = ["Beer","Type","ABV","Manufacturers","Food","Taste","Price","Volume","Untappd rating"] # Beer table columns
    row_counter = 0

    for row in beer_info: #Prints the column and the propper vaule. 
        for info in row:
            print(f"{column[row_counter]}: {info}")
            row_counter += 1
    
    #If the fetch doesn't get any data the program should act accordingly
    if row_counter == 0:
        print("Sorry, the database doens't have that beer.")
        input("Press enter to go back to the main menu: ")
    else:
        user_input = input(
            "-----------------------------------------\n"
            "1. Search more about a certain beer\n"
            "-----------------------------------------\n"
            "Please choose a option or press enter to return to the main menu: "
        )
        if user_input == "1":
            option_nine()
        else:
            pass

#Ask for a beer input and the return the brewery that makes the beer and the country where the brewery is located/started.4
def option_ten():
    beer_input = input("What beer are you woundering about? ")
    cursor.execute(
        "SELECT brewery, country "
        "FROM sour JOIN brewery ON sour.manufacturers = brewery.brewery " 
        f"WHERE sour.beer = '{beer_input}'"
        "UNION "
        "SELECT brewery, country "
        "FROM stout JOIN brewery ON stout.manufacturers = brewery.brewery " 
        f"WHERE stout.beer = '{beer_input}'"
        "UNION "
        "SELECT brewery, country "
        "FROM wheat JOIN brewery ON wheat.manufacturers = brewery.brewery " 
        f"WHERE wheat.beer = '{beer_input}'"
        "UNION "
        "SELECT brewery, country "
        "FROM lager JOIN brewery ON lager.manufacturers = brewery.brewery " 
        f"WHERE lager.beer = '{beer_input}'"
        "UNION "
        "SELECT brewery, country "
        "FROM ale JOIN brewery ON ale.manufacturers = brewery.brewery " 
        f"WHERE ale.beer = '{beer_input}'"
    )
    country_brewery = cursor.fetchall()
    lst_info = ["Brewery","Country"]
    index_value = 0
    row_counter = 0
    
    #Prints the column and the propper vaule. 
    for row in country_brewery: 
        for info in row:
            print(f"{lst_info[index_value]}: {info}")
            index_value += 1
        row_counter += 1

    #If the fetch doesn't get any data the program should act accordingly
    if row_counter == 0:
        print("Sorry, the database doens't have that brewery.")
        input("Press enter to go back to the main menu: ")
    else:
        user_input = input(
            "-----------------------------------------\n"
            "1. Search more about a certain brewery\n"
            "-----------------------------------------\n"
            "Please choose a option or press enter to return to the main menu: "
        )
        if user_input == "1":
            option_seven()
        else:
            pass

# MAIN

#Creates beer database
try:
    cursor.execute("USE {}".format(DB_NAME)) 

# If the database doesn't exsist the program creates the new database.
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))

    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor, DB_NAME)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
        create_table_brewery(cursor)
        create_table_ale(cursor)
        create_table_lager(cursor)
        create_table_sour(cursor)
        create_table_stout(cursor)
        create_table_wheat(cursor)
        view_one()
    else:
        print(err)

try:
    while True: # Runs the the progam until the input is q or Q
        mainmenu()
        option_input = str(input("Please choose one option: "))
        if option_input == "1":
            option_one()
        elif option_input == "2":
            option_two()
        elif option_input == "3":
            option_three()
        elif option_input == "4":
            option_four()
        elif option_input == "5":
            option_five()
        elif option_input == "6":
            option_six() 
        elif option_input == "7":
            option_seven()
        elif option_input == "8":
            option_eight()
        elif option_input == "9":
            option_nine()
        elif option_input == "10":
            option_ten()
        elif option_input == "Q" or option_input == "q":
            print("Thank you for using Drinking Buddy!")
            exit(1)
        else:
            print("Wrong input, try again")
            input("Please press enter to return to the main menu. ")

except Exception as err:
    print(err)