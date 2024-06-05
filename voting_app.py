import re

class VotingApp:
    def __init__(self):
        self.voters = []
        self.used_nida_numbers = set()
    
    def is_valid_nida(self, nida):
        return re.match(r'^\d{15}$', nida) and nida not in self.used_nida_numbers
    
    def register_voter(self):
        name = input("Enter your name: ")
        
        while True:
            try:
                age = int(input("Enter your age: "))
                if age < 18:
                    print("You must be at least 18 years old to vote.")
                    return
                break
            except ValueError:
                print("Please enter a valid age.")
        
        country = input("Enter your country: ")
        city = input("Enter your city: ")
        
        while True:
            nida = input("Enter your 15-digit NIDA number: ")
            if not self.is_valid_nida(nida):
                print("Invalid NIDA number. Make sure it is 15 digits long and not previously used.")
            else:
                break
        
        voter = {
            "name": name,
            "age": age,
            "country": country,
            "city": city,
            "nida": nida
        }
        
        self.voters.append(voter)
        self.used_nida_numbers.add(nida)
        print("Voter registered successfully!")

    def show_voters(self):
        print("Registered Voters:")
        for voter in self.voters:
            print(f"Name: {voter['name']}, Age: {voter['age']}, Country: {voter['country']}, City: {voter['city']}, NIDA: {voter['nida']}")

# Instantiate the VotingApp
app = VotingApp()

while True:
    print("1. Register to vote")
    print("2. Show registered voters")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        app.register_voter()
    elif choice == '2':
        app.show_voters()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
