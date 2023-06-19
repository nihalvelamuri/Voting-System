
import random
import string


class User:
    def __init__(self, username, password, name="", aadhar_number="", area="", phone_number="", age=0):
        self.username = username
        self.password = password
        self.name = name
        self.aadhar_number = aadhar_number
        self.area = area
        self.phone_number = phone_number
        self.age = age


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_user(self, user): 
        node = SinglyLinkedListNode(user)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def find_user(self, username):
        current = self.head
        while current:
            if current.data.username == username:
                return current.data
            current = current.next
        return None

    def remove_user(self, username):
        if not self.head:
            return

        if self.head.data.username == username:
            self.head = self.head.next
            return

        prev = self.head
        current = self.head.next
        while current:
            if current.data.username == username:
                prev.next = current.next
                return
            prev = current
            current = current.next


class VotingSystem:
    def __init__(self):
        self.admin_credentials = SinglyLinkedList()
        self.candidate_credentials = SinglyLinkedList()
        self.voter_credentials = SinglyLinkedList()
        self.votes = {}
        self.voted_voters = set()  # Set to track voted voters

        # Adding a default admin for testing purposes
        admin = User("admin", "admin")
        self.admin_credentials.add_user(admin)

    def login(self, username, password):
        admin = self.admin_credentials.find_user(username)
        candidate = self.candidate_credentials.find_user(username)
        voter = self.voter_credentials.find_user(username)

        if admin and admin.password == password:
            return "admin"
        elif candidate and candidate.password == password:
            return "candidate"
        elif voter and voter.password == password:
            return "voter"
        else:
            return None
        
    def display_candidates(self):
        print("\n----- Available Candidates -----")
        current = self.candidate_credentials.head
        while current:
            candidate = current.data
            print(f"Username: {candidate.username}")
            print(f"Name: {candidate.name}")
            print(f"Aadhar Number: {candidate.aadhar_number}")
            print(f"Area: {candidate.area}")
            print("----------------------")
            current = current.next


    def login_menu(self):
        while True:
            print("----- Login Menu -----")
            print("1. Login as Admin")
            print("2. Login as Candidate")
            print("3. Login as Voter")
            print("4. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.admin_login()
            elif choice == "2":
                self.candidate_login()
            elif choice == "3":
                self.voter_login()
            elif choice == "4":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

    def admin_login(self):
        print("\n----- Admin Login -----")
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_role = self.login(username, password)

        if user_role == "admin":
            self.admin_menu()
        else:
            print("Login failed. Invalid username or password.")

    def candidate_login(self):
        print("\n----- Candidate Login -----")
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_role = self.login(username, password)

        if user_role == "candidate":
            self.candidate_menu(username)
        else:
            print("Login failed. Invalid username or password.")

    def voter_login(self):
        print("\n----- Voter Login -----")
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_role = self.login(username, password)

        if user_role == "voter":
            self.voter_menu(username)
        else:
            print("Login failed. Invalid username or password.")

    def admin_menu(self):
        while True:
            print("\n----- Admin Menu -----")
            print("1. Add Candidate")
            print("2. Add Voter")
            print("3. View Candidates")
            print("4. View Voters")
            print("5. View Votes")
            print("6. Edit Candidate Info")
            print("7. Edit Voter Info")
            print("8. Remove Candidate")
            print("9. Remove Voter")
            print("10. Declare Results")
            print("11. Logout")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_candidate()
            elif choice == "2":
                self.add_voter()
            elif choice == "3":
                self.view_candidates()
            elif choice == "4":
                self.view_voters()
            elif choice == "5":
                self.view_votes()
            elif choice == "6":
                username = input("Enter candidate username to edit info: ")
                self.edit_candidate_info(username)
            elif choice == "7":
                username = input("Enter voter username to edit info: ")
                self.edit_voter_info(username)
            elif choice == "8":
                username = input("Enter candidate username to remove: ")
                self.remove_candidate(username)
            elif choice == "9":
                username = input("Enter voter username to remove: ")
                self.remove_voter(username)
            elif choice == "11":
                print("Returning to login menu.")
                break
            elif choice == "10":
                self.declare_results()
            else:
                print("Invalid choice. Please try again.")
            
    def view_personal_information(self, username):
        candidate = self.candidate_credentials.find_user(username)
        if candidate:
            print("\n----- Candidate Personal Information -----")
            print(f"Username: {candidate.username}")
            print("------------------------------------------")
        else:
            voter = self.voter_credentials.find_user(username)
            if voter:
                print("\n----- Voter Personal Information -----")
                print(f"Username: {voter.username}")
                print("--------------------------------------")
            else:
                print("User not found.")
                
    def declare_results(self):
        print("\n----- Declare Results -----")
        if self.votes:
            winner = max(self.votes, key=self.votes.get)
            max_votes = self.votes[winner]
            print(f"{winner} has won with {max_votes} votes")
        else:
            print("No votes found.")

            

    def add_candidate(self):
        print("\n----- Add Candidate -----")
        username = input("Enter username: ")
        password = input("Enter password: ")
        name = input("Enter candidate name: ")
        aadhar_number = input("Enter candidate Aadhar number: ")
        area = input("Enter candidate area: ")

        candidate = User(username, password, name, aadhar_number, area)
        self.candidate_credentials.add_user(candidate)
        print(f"Candidate '{name}' added successfully!")
        print(f"Username: {username}")
        print(f"Password: {password}")
        
    def edit_voter_info(self, username):
        voter = self.voter_credentials.find_user(username)
        if voter:
            print(f"\n----- Edit Voter Info -----")
            print(f"Current Name: {voter.name}")
            voter.name = input("Enter new name: ")
            print(f"Current Aadhar Number: {voter.aadhar_number}")
            voter.aadhar_number = input("Enter new Aadhar number: ")
            print(f"Current Area: {voter.area}")
            voter.area = input("Enter new area: ")
            print(f"Current Phone Number: {voter.phone_number}")
            voter.phone_number = input("Enter new phone number: ")
            print(f"Current Age: {voter.age}")
            voter.age = int(input("Enter new age: "))
            print("Voter info updated successfully!")
        else:
            print("Voter not found.")

    def edit_candidate_info(self, username):
        candidate = self.candidate_credentials.find_user(username)
        if candidate:
            print(f"\n----- Edit Candidate Info -----")
            print(f"Current Name: {candidate.name}")
            candidate.name = input("Enter new name: ")
            print(f"Current Aadhar Number: {candidate.aadhar_number}")
            candidate.aadhar_number = input("Enter new Aadhar number: ")
            print(f"Current Area: {candidate.area}")
            candidate.area = input("Enter new area: ")
            print("Candidate info updated successfully!")
        else:
            print("Candidate not found.")
        
    def add_voter(self):
        print("\n----- Add Voter -----")
        username = input("Enter username: ")
        password = input("Enter password: ")
        name = input("Enter voter name: ")
        aadhar_number = input("Enter voter Aadhar number: ")
        area = input("Enter voter area: ")
        phone_number = input("Enter voter phone number: ")
        age = int(input("Enter voter age: "))

        if age < 18:
            print("Voter's age should be 18 or above to register.")
            return

        voter = User(username, password, name, aadhar_number, area, phone_number, age)
        self.voter_credentials.add_user(voter)
        print(f"Voter '{name}' added successfully!")
        print(f"Username: {username}")
        print(f"Password: {password}")


    def remove_candidate(self, username):
        candidate = self.candidate_credentials.find_user(username)
        if candidate:
            self.candidate_credentials.remove_user(username)
            print(f"Candidate '{username}' removed successfully!")
        else:
            print("Candidate not found.")

    def remove_voter(self, username):
        voter = self.voter_credentials.find_user(username)
        if voter:
            self.voter_credentials.remove_user(username)
            print(f"Voter '{username}' removed successfully!")
        else:
            print("Voter not found.")
            
    def edit_information(self, username):
        candidate = self.candidate_credentials.find_user(username)
        if candidate:
            print("\n----- Edit Candidate Information -----")
            password = input("Enter new password (leave blank to keep existing): ")
            if password:
                candidate.password = password
            print("Candidate information updated successfully.")
        else:
            voter = self.voter_credentials.find_user(username)
            if voter:
                print("\n----- Edit Voter Information -----")
                password = input("Enter new password (leave blank to keep existing): ")
                if password:
                    voter.password = password
                print("Voter information updated successfully.")
            else:
                print("User not found.")

    def view_candidates(self):
        print("\n----- Candidates -----")
        current = self.candidate_credentials.head
        while current:
            candidate = current.data
            print(f"Username: {candidate.username}")
            print(f"Name: {candidate.name}")
            print(f"Aadhar Number: {candidate.aadhar_number}")
            print(f"Area: {candidate.area}")
            print("----------------------")
            current = current.next
            
    def view_voters(self):
        print("\n----- Voters -----")
        current = self.voter_credentials.head
        while current:
            voter = current.data
            print(f"Username: {voter.username}")
            print(f"Name: {voter.name}")
            print(f"Aadhar Number: {voter.aadhar_number}")
            print(f"Area: {voter.area}")
            print(f"Phone Number: {voter.phone_number}")
            print(f"Age: {voter.age}")
            print("-----------------")
            current = current.next

 #   def view_votes(self):
  #      print("\n----- Votes -----")
   #     for candidate_username, vote_count in self.votes.items():
    #        print(f"Candidate: {candidate_username}, Votes: {vote_count}")
            
    def view_votes(self):
        print("\n----- Votes -----")
        for candidate, count in self.votes.items():
            print(f"Candidate: {candidate}")
            print(f"Vote Count: {count}")
            print("-----------------")

    def candidate_menu(self, username):
        while True:
            print("\n----- Candidate Menu -----")
            print("1. View Profile")
            print("2. Logout")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.view_candidate_profile(username)
            elif choice == "2":
                print("Returning to login menu.")
                break
            else:
                print("Invalid choice. Please try again.")

    def view_candidate_profile(self, username):
        candidate = self.candidate_credentials.find_user(username)
        if candidate:
            print("\n----- Candidate Profile -----")
            print(f"Username: {candidate.username}")
            print(f"Name: {candidate.name}")
            print(f"Aadhar Number: {candidate.aadhar_number}")
            print(f"Area: {candidate.area}")
        else:
            print("Candidate not found.")

    def voter_menu(self, username):
        while True:
            print("\n----- Voter Menu -----")
            print("1. View Profile")
            print("2. Vote for a Candidate")
            print("3. Logout")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.view_voter_profile(username)
            elif choice == "2":
                self.vote_for_candidate(username)
            elif choice == "3":
                print("Returning to login menu.")
                break
            else:
                print("Invalid choice. Please try again.")

    def view_voter_profile(self, username):
        voter = self.voter_credentials.find_user(username)
        if voter:
            print("\n----- Voter Profile -----")
            print(f"Username: {voter.username}")
            print(f"Name: {voter.name}")
            print(f"Aadhar Number: {voter.aadhar_number}")
            print(f"Area: {voter.area}")
            print(f"Phone Number: {voter.phone_number}")
            print(f"Age: {voter.age}")
        else:
            print("Voter not found.")

    def vote_for_candidate(self, username):
        if username in self.voted_voters:
            print("You have already voted. You cannot vote again.")
            return

        print("\n----- Vote for a Candidate -----")
        self.display_candidates()  # Display the list of available candidates

        candidate_username = input("Enter the username of the candidate you want to vote for: ")
        candidate = self.candidate_credentials.find_user(candidate_username)
        if candidate:
            if candidate_username in self.votes:
                self.votes[candidate_username] += 1
            else:
                self.votes[candidate_username] = 1

            self.voted_voters.add(username)  # Add the username to the voted voters set
            print("Vote cast successfully!")
        else:
            print("Candidate not found.")


    def voter_registration(self):
        print("\n----- Voter Registration -----")
        username = input("Enter username: ")
        password = input("Enter password: ")
        name = input("Enter your name: ")
        aadhar_number = input("Enter your Aadhar number: ")
        area = input("Enter your area: ")
        phone_number = input("Enter your phone number: ")
        age = int(input("Enter your age: "))

        existing_user = self.voter_credentials.find_user(username)
        if existing_user:
            print("Username already exists. Please choose a different username.")
            return

        voter = User(username, password, name, aadhar_number, area, phone_number, age)
        self.voter_credentials.add_user(voter)
        print("Voter registered successfully!")


voting_system = VotingSystem()
voting_system.login_menu()