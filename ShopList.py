shopping_list = ["Banana","Orange","Blueberry", "Broccoli", "Cereal"]

def shopping_menu():
    print("what would you like to do to your list")
    print("""
Enter ADD to add to the list
Enter REMOVE to remove from list 
Enter DONE to quit the list
Enter SHOW to see your list""")

def add():
    print("What would you like to add?")
    new_item = input("Item: ")
    shopping_list.append(new_item)

def show_list():
    if len(shopping_list) == 0:
        print("Theres nothing here")
    else:
        print("Items in list \n")
        for items in shopping_list:
            print(items)

def remove():
    print("Which item would you like to remove?")
    item = input("Item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print("That item is not on your list")
    
shopping_menu()


while True:
    item = input("Chose an option: ")
    if item == "DONE":
        print("All done")
        break
    elif item == "REMOVE":
        remove()
    elif item == "ADD":
        add()
    elif item == "SHOW":
        show_list()
        



