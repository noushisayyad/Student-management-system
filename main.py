def show_menu():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Add student feature coming soon...")
        elif choice == "2":
            print("View students feature coming soon...")
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
