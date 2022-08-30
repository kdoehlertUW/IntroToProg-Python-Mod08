# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# KDoehlert,8.29.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
        __str__(self): -> (string) with product name and product price

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        KDoehlert,8.28.2022,Modified code to complete assignment 8
    """

    # Constructor
    def __init__(self, product_name, product_price):

        # Attributes (these just reference the properties)
        self.product_name = product_name
        self.product_price = product_price

    # Properties
    # Product Name
    @property # getter for Product Name
    def product_name(self):
        return self.__str_product_name

    @product_name.setter # setter for Product Name
    def product_name(self, value):
        self.__str_product_name = value

    # Product Price
    @property # getter for Product Price
    def product_price(self):
        return self.__flt_product_price # validation occurs in IO.input_add_product_data

    @product_price.setter # setter for Product Price
    def product_price(self, value):
        self.__flt_product_price = value # validation occurs in IO.input_add_product_data

    # Methods
    def __str__(self):
        """ Prints product name and price when product object is printed

                :param: self:
                :return: nothing:
        """
        return self.product_name + "," + str(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (list) of product objects

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        KDoehlert,8.28.2022,Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Writes data from a list of product objects to a File

        :param file_name: (string) with name of file:
        :param list_of_product_objects: (list) you want filled with file data:
        """
        file = open(file_name, "w")
        for obj in list_of_product_objects:
            file.write(str(obj) + "\n") #  writes each object in the list using __str__ method to a new line of the file
        file.close()

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :return: (list) of product objects rows:
        """
        list_of_product_objects = []
        try: # reads data if file exists
            file = open(file_name, "r")
            for line in file:
                name, price = line.split(",") #unpacks comma separated list to name and price
                product = Product(name.strip(),price.strip()) # creates new Product object with name and price
                list_of_product_objects.append(product) # adds new Product object to list of products
            file.close()
        except FileNotFoundError as e: #error handling if file does not exist
            print()  # blank line for formatting
            print("File does not exist. There is no data to load.\n")
        return list_of_product_objects

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Performs Input and Output tasks:

    methods:
        output_menu_choices():
        input_menu_choice(): -> (string) with menu choice
        output_show_data_from_file(list_of_product_objects)
        input_add_product_data() -> (string, float) with product name and price

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        KDoehlert,8.28.2022,Modified code to complete assignment 8
    """

    @staticmethod
    def output_menu_choices():
        """ Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show Current Products
        2) Add a New Product
        3) Save Data to File        
        4) Exit Program
        ''')
        print()

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: (string) with menu choice:
        """
        choice = input("Which option would you like to perform? [1 to 4] - ").strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_product_data(list_of_product_objects):
        """ Shows the current product names and prices

        :param list_of_product_objects: (list) of objects that was read from file
        :return: nothing
        """
        if list_of_product_objects == []: # handles cases when products have not yet been added
            print('There are no Products to show.')
        else:
            for object in list_of_product_objects:
                # loops through each Product object in list and uses product_name and product_price properties
                # to get private variables
                print('Product Name: ' + object.product_name.title() + '\nProduct Price: $'
                      + str(object.product_price) + '\n')

    @staticmethod
    def input_add_product_data():
        """  Gets name and price values to be added to the list

        :return: (string, float) with product name and price
        """
        product_name = None
        product_price = None
        # continues looping until there is a valid entry for both name and price
        while product_name == None or product_price == None:
            try:
                product_name = input("Enter a Product to add: ")
                if product_name.isnumeric() == True: # checks to see if name is a number and raises error if true
                    raise Exception('Product not added. Product Name cannot be a number.')
                product_price = float(input("Enter the Price of the Product: "))

            # ValueError will be raised when trying to convert input to float if product_price is not a number
            except ValueError as e:
                print()
                print('Product not added. Please enter a number [12.34] for the Price.')
                print()
            except: # this message will be used if error is not ValueError
                print()
                print('Product not added. Product Name cannot be a number.')
                print()
        print()
        return product_name,product_price

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Loads data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(file_name=strFileName)

# Loops until break is hit when 4 is entered
while (True):

    # Show user a menu of options
    IO.output_menu_choices()

    # Get user's menu option choice
    choice_str = IO.input_menu_choice()

    # Show user current data in the list of product objects
    if choice_str.strip() == '1':
        IO.output_product_data(list_of_product_objects = lstOfProductObjects)
        continue

    # Let user add data to the list of product objects
    elif choice_str.strip() == '2':
        #  unpacks product_name and product_price to be used below
        product_name, product_price = IO.input_add_product_data()
        # creates new Product object from name and price returned from IO.input_add_product_data()
        product_object = Product(product_name,product_price)
        # adds new Product object to list of objects
        lstOfProductObjects.append(product_object)
        print('Your Product has been added.')
        continue

    # let user save current data to file and exit program
    elif choice_str.strip() == '3': # saves data
        FileProcessor.save_data_to_file(strFileName,lstOfProductObjects)
        print('Your data has been saved.')
        continue

    elif choice_str.strip() == '4': # exits program
        print('Goodbye!')
        break # exits loop

    else:
        print('\nPlease make a selection 1 - 4') # handles situations when users give invalid input

# Main Body of Script  ---------------------------------------------------- #