This Python code represents a basic voting system implemented using object-oriented programming principles. It includes three main classes: `User`, `SinglyLinkedList`, and `VotingSystem`. Here's a brief description of each class and the navigation within the system:

1. `User` Class:
   - This class defines the attributes of a user, including `username`, `password`, `name`, `aadhar_number`, `area`, `phone_number`, and `age`.
   - Users can be of three types: Admin, Candidate, and Voter.

2. `SinglyLinkedList` Class:
   - This class defines a singly-linked list data structure that stores user objects (Admin, Candidate, or Voter).
   - It provides methods to add, find, and remove users in the linked list.

3. `VotingSystem` Class:
   - This class represents the main voting system and orchestrates the entire voting process.
   - It contains separate linked lists for admin, candidate, and voter credentials.
   - It tracks votes and ensures that voters can vote only once by using a set called `voted_voters`.

Navigation within the system:

- The program starts by creating an instance of the `VotingSystem` class and adding a default admin user for testing purposes.
- The `login_menu()` function presents a menu for users to choose their role (Admin, Candidate, or Voter) and log in.
- Once logged in, each user type (Admin, Candidate, or Voter) has access to specific menus and actions:
   - Admin:
     - Can add and remove candidates and voters.
     - Can view the list of candidates and voters.
     - Can edit candidate and voter information.
     - Can declare election results.
     - Can log out to return to the login menu.
   - Candidate:
     - Can view their profile information.
     - Can log out to return to the login menu.
   - Voter:
     - Can view their profile information.
     - Can vote for a candidate (once) from the list of available candidates.
     - Can log out to return to the login menu.

Overall, this code demonstrates a simple command-line-based voting system with user authentication, candidate registration, voter registration, and vote-counting capabilities. Users are authenticated based on their roles, and the system ensures that voters can cast their votes only once.
