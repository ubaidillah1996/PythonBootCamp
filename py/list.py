grocery_list = [] 

while True:
    print("Grocery List Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Clear list")
    print("5. Exit")   

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        item = input("Enter the item to add: ")
        grocery_list.append(item) # append : tambah
        print(f"{item} added to the list.")
    
    elif choice == '2':
        item = input("Enter the item to remove: ")
        if item in grocery_list:
            grocery_list.remove(item)
            print(f"{item} removed from the list.")
        else:
            print(f"{item} is not in the list.") # semak ada atau tidak barang tu 
    
    elif choice == '3':
        if grocery_list:
            print("Grocery List:")
            for i, item in enumerate(grocery_list, start=1):
                print(f"{i}. {item}") # enumerate : dah siap susun teratur.
        else:
            print("The grocery list is empty.")
    
    elif choice == '4':
        grocery_list.clear() # clear : kosongkan list
        print("Grocery list cleared.")
    
    elif choice == '5':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Try again.")