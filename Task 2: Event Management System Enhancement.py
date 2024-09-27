class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  
    
    def add_participant(self):
        self.participant_count += 1
        print(f"A ticket was purchased for the '{self.name}'. \nTotal participants: {self.participant_count}\n")
    
    def get_participant_count(self):
        return self.participant_count

concert = Event("Range Day Event", "09/28/2024")

print(f"\nInitial participant count for '{concert.name}': {concert.get_participant_count()}\n")


concert.add_participant()
concert.add_participant()
concert.add_participant()

print(f"Updated participant count for '{concert.name}': {concert.get_participant_count()}\n")