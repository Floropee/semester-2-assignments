class  FitnessClass:
    gym_name= "Power Gym"
    max_capacity = 3
    total_classes = 0
    
    def __init__(self, class_name, instructor):
        self.class_name=class_name
        self.instructor=instructor
        self.participants=[]
        FitnessClass.total_classes+=1
        
    def add_participant(self,name):
        if len(self.participants)<FitnessClass.max_capacity:
            self.participants.append(name)
            print(f"Added {name} to {self.class_name}")
        else:
            print("Class is full")
    
    def remove_participant(self,name):
        if name in self.participants:
            self.participants.remove(name)
            print(f"Removed {name} from {self.class_name}")
        else:
            print("Participant not found")
            
    def display_class(self):
        print(f"Class: {self.class_name}, Instructor: {self.instructor}, Gym: {FitnessClass.gym_name}")

yoga=FitnessClass('Yoga', 'Malika')
yoga.display_class()
yoga.add_participant('Ali')
yoga.add_participant('Vali')
yoga.add_participant('Gulnora')
yoga.add_participant('Rustam')
yoga.remove_participant('Vali')
yoga.remove_participant('Sarvar')
print(f"Total classes: {FitnessClass.total_classes}")