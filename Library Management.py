print("LIBRARY MANAGEMENT SYSTEM")



# LIBRARY MANAGEMENT SYSTEM
# 1. Display all books
# 2. Borrow a book
# 3. Return a book
# 4. Check book status
# 5. Exit
# 6. Request a Book
# 7. Delete a book
# 8. Update a book

RequestedBook = None
RequestedBookStatus = "Available"

Book1 = "Harry Potter"
Book2 = "Lord of the rings"
Book3 = "The Hobbit"
Book4 = "The Great Gatsby"
Book5 = "The Alchemist"

Book1_Status = "Available"
Book2_Status = "Available"
Book3_Status = "Available"
Book4_Status = "Available"
Book5_Status = "Available"

while True:
    print ( "\n" "Welcome to the Library Management System")
    print ("-----------------------------------------")
    print ("1. Display all books")
    print ("2. Borrow a book")
    print ("3. Return a book")
    print ("4. Check book status") # SEARCHING
    print ("5. Exit")
    print ("6. Add a new book")
    print ("7. Delete a book")
    print ("8. Update a book")

    option = int (input("Enter your choice (1-8): "))

    if option == 5:
        print("Exiting the system...")
        break

    elif option == 6:
        if RequestedBook is None:
            NewBook = input ( "\n" "Enter the book name you want to add:" "\n")
            # SWAPPING 
            RequestedBook = NewBook
            RequestedBookStatus = "Available"
            print ( "\n" "Book added successfully")

    elif option == 1:
        print (" \n " "List of available books:")
        print (Book1 + " - " + Book1_Status)
        print (Book2 + " - " + Book2_Status)
        print (Book3 + " - " + Book3_Status)
        print (Book4 + " - " + Book4_Status)
        print (Book5 + " - " + Book5_Status)

        if RequestedBook:
            print (RequestedBook + " - " + RequestedBookStatus)

    elif option == 2: #Borrow a book
        BookName = input("\n" "Enter the name of the book you want to borrow:" "\n")

        if BookName == Book1 and Book1_Status == "Available":
            print ( "\n" "You have borrowed " + Book1)
            Book1_Status = "Not Available"

        elif BookName == Book2 and Book2_Status == "Available":
            print ("You have borrowed " + Book2)
            Book2_Status = "Not Available"

        elif BookName == Book3 and Book3_Status == "Available":
            print ("You have borrowed " + Book3)
            Book3_Status = "Not Available"

        elif BookName == Book4 and Book4_Status == "Available":
            print ("You have borrowed " + Book4)
            Book4_Status = "Not Available"

        elif BookName == Book5 and Book5_Status == "Available":
            print ("You have borrowed " + Book5)
            Book5_Status = "Not Available"

        elif BookName == NewBook and RequestedBookStatus == "Available":
            print ( "\n" "You have borrowed " + NewBook)
            RequestedBookStatus = "Not Available"

        else:
            print ("Book not available")

    elif option == 3: #Return a Book

        BookName = input("\n" "Enter the name of the book you want to return:" "\n" )

        if BookName == Book1 and Book1_Status == "Not Available":
            print ("\n" "You have returned " + Book1 , "\n")
            Book1_Status = "Available"

        elif BookName == Book2 and Book2_Status == "Not Available":
            print ("You have returned " + Book2 , "\n")
            Book2_Status = "Available"

        elif BookName == Book3 and Book3_Status == "Not Available":
            print ("You have returned " + Book3 , "\n")
            Book3_Status = "Available"

        elif BookName == Book4 and Book4_Status == "Not Available":
            print ("You have returned " + Book4 , "\n")
            Book4_Status = "Available"

        elif BookName == Book5 and Book5_Status == "Not Available":
            print ("You have returned " + Book5 , "\n")
            Book5_Status = "Available"

        elif BookName == NewBook and RequestedBookStatus == "Not Available":
            print ( "\n" "You have returned " + NewBook , "\n")
            RequestedBookStatus = "Available"

        else:
            print ("Book was not borrowed")

    elif option == 4: # Check Book Status
        BookName = input("\n" "Enter the name of the book you want to check:" "\n" )

        if BookName == Book1:
            print ("Book1: " , Book1 , "is" , Book1_Status)

        elif BookName == Book2:
            print ("Book2: " , Book2 , "is" , Book2_Status)

        elif BookName == Book3:
            print ("Book3: " , Book3 , "is" , Book3_Status)

        elif BookName == Book4:
            print ("Book4: " , Book4 , "is" , Book4_Status)

        elif BookName == Book5:
            print ("Book5: " , Book5 , "is" , Book5_Status)

        elif BookName == NewBook:
            print ("New Book: " , NewBook , "is" , RequestedBookStatus)

        else:
            print ("We don't have that book.")
    elif option == 7:
        Deleted_book = str(input("Which book would you like to delete")) 
        if Deleted_book == Book1 and Book1_Status == "Available"and"Not Available":
            print("We have deleted the book")
            Book1_Status = "The book has been removed"

        elif Deleted_book == Book2 and Book2_Status == "Available "and"Not Available":
            print("We have deleted the book")
            Book2_Status = "The book has been removed"

        elif Deleted_book == Book3 and Book3_Status == "Available "and"Not Available":
            print("We have deleted the book")
            Book3_Status = "The book has been removed"
        
        elif Deleted_book == Book4 and Book4_Status == "Available "and"Not Available":
            print("We have deleted the book")
            Book4_Status = "The book has been removed"
        
        elif Deleted_book == Book5 and Book5_Status == "Available "and"Not Available":
            print("We have deleted the book")
            Book5_Status = "The book has been removed"

        elif BookName == NewBook and RequestedBookStatus == "Available" and "Not Available":
            print ("We have deleted the book")
            RequestedBookStatus = "The book has been removed" 
    

    elif option == 8: 

        BookName = input("\n" "Enter the name of the book you want to update:" "\n" )

        if BookName == Book1 and Book1_Status == "Available":
            print ("We have updated the book: " + Book1 , "\n")
            Book1_Status = "Available (Updated)"
        
        elif BookName == Book2 and Book2_Status == "Available":
            print ("We have updated the book: " + Book2 , "\n")
            Book2_Status = "Available (Updated)"

        elif BookName == Book3 and Book3_Status == "Available":
            print ("We have updated the book: " + Book3 , "\n")
            Book3_Status = "Available (Updated)"

        elif BookName == Book4 and Book4_Status == "Available":
            print ("We have updated the book: " + Book4 , "\n")
            Book4_Status = "Available (Updated)"

        elif BookName == Book5 and Book5_Status == "Available":
            print ("We have updated the book: " + Book5 , "\n")
            Book5_Status = "Available (Updated)"

        elif BookName == NewBook and RequestedBookStatus == "Available":
            print ("We have updated the book")
            RequestedBookStatus = "Available (Updated)" 


        
    else:
        print ("Invalid option. Please choose a valid option")