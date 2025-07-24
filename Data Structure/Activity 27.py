class Dog:
    # Class variable: This variable is shared by all instances of the Dog class.
    species = "Canis familiaris"

    def __init__(self, name, breed):
        # Instance variables: These variables are unique to each instance of the Dog class.
        self.name = name
        self.breed = breed

    def display_details(self):
        """
        Displays the details of the dog.
        """
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}") # Accessing the class variable

# Create two instances of the Dog class for different breeds
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "German Shepherd")

# Display the details of the first dog
print("Details of Dog 1:")
dog1.display_details()
print("-" * 20)

# Display the details of the second dog
print("Details of Dog 2:")
dog2.display_details()