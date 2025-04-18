from pet import Pet

def main():
    print("Welcome to the Virtual Pet Simulator!")
    pet_name = input("What would you like to name your pet? ")
    my_pet = Pet(pet_name)
    
    while True:
        my_pet.get_status()
        print("What would you like to do?")
        print("1. Feed your pet")
        print("2. Put your pet to sleep")
        print("3. Play with your pet")
        print("4. Teach your pet a trick")
        print("5. See learned tricks")
        print("6. Quit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            my_pet.eat()
        elif choice == "2":
            my_pet.sleep()
        elif choice == "3":
            my_pet.play()
        elif choice == "4":
            trick = input("What trick would you like to teach? ")
            my_pet.train(trick)
        elif choice == "5":
            my_pet.show_tricks()
        elif choice == "6":
            print(f"Goodbye! Take care of {my_pet.name}!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()