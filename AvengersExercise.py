import itertools

class Avengers:
    # Initialize values to self, (reference to instance).
    def __init__(self,name,age,gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    # Method will print description of super hero by referencing the current instance of the Avengers class
    def hero_description(self):
        print(f"Hero Name: {self.name}")
        print(f"Hero Age: {self.age}")
        print(f"Hero Gender: {self.gender}")
        print(f"Hero Super Power: {self.super_power}")
        print(f"Hero Weapon: {self.weapon}")

    # Method will reference instance of class to see if current Avenger is the leader or not
    # If current instance of class's name isn't equal to 'Captain America', print 'No'
    # If current instance of class's name is equal to 'Captain America', print 'Yes'
    def is_leader(self):
        if self.name == "Captain America":
            print("Leader: Yes")
        else:
            print("Leader: No")

    def update_dict(self):
        dict = {f"{self.name}": f"{self.age}, {self.gender}, {self.super_power}, {self.weapon}"}
        return dict

# Main function
def main():
    # Create lists of Avenger attributes that correspond with each other
    super_heroes = ['Captain America','Iron Man','Black Widow','Hulk','Thor','Hawkeye']
    hero_ages = [82,50,32,49,1500,41]
    hero_genders = ['Male','Male','Female','Male','Male','Male']
    hero_super_power = ['Super Strength','Technology','Super Human','Unlimited Strength','Energy','Fighting Skills']
    hero_weapon = ['Shield','Armor','Batons','No Weapon','Mjolnir','Bow and Arrows']

    hero_dict = {} # Dictionary which will store about superheroes for increased readability/accessibility

    # Iterates through each list simultaneously using itertools module
    for (name,age,gender,super_power,weapon) in zip(super_heroes,hero_ages,hero_genders,hero_super_power,hero_weapon):
        # Create instance of Avengers class that will pass Avenger information to class
        obj = Avengers(name,age,gender,super_power,weapon)
        obj.hero_description() # Access method in class which will print current hero description
        obj.is_leader() # Access method in class which determines if current Avenger is leader or not
        hero_dict.update(obj.update_dict()) # Updates dictionary with key-value pairs
        print() # Print whitespace to separate each iteration

# Execute main function
main()
