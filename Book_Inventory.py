# Create an empty dictionary to store books and their stock
book_stock = {}

while True:
    print("\n--- Book Inventory Menu ---")
    print("1. Add or Update Book")
    print("2. Delete Book")
    print("3. Show All Books")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        book_name = input("Enter the book name: ")
        stock = input("Enter the stock quantity: ")
        
        # check the stock is digit or not
        if stock.isdigit():
            stock = int(stock)
            book_stock[book_name] = stock
            print(f"Book '{book_name}' added/updated with {stock} copies.")
        else:
            print("Please enter a valid number for stock.")

    elif choice == "2":
        book_name = input("Enter the book name to delete: ")
        if book_name in book_stock:
            del book_stock[book_name]
            print(f"Book '{book_name}' deleted.")
        else:
            print("Book not found in inventory.")

    elif choice == "3":
       print(book_stock)

    elif choice == "4":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")



