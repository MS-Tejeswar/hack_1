#!/usr/bin/env python
# coding: utf-8

# In[6]:


import datetime
import random

class EWasteMonitoringSystem:
    def __init__(self):
        self.items = []
        self.schedule = []

    def add_item(self, name, category, age, condition, energy_consumption):
        item = {
            'name': name,
            'category': category,
            'age': age,
            'condition': condition,
            'energy_consumption': energy_consumption,
            'added_date': datetime.datetime.now()
        }

        recommendation = self._generate_recommendation(item)
        print(f"Recommendation: {recommendation}\n")
        
        if 'recycled' in recommendation:
            self.schedule_recycling(item)
        else:
            self.items.append(item)
            print(f"{name} has been added to the E-waste monitoring system.\n")

    def _generate_recommendation(self, item):
        if item['age'] > 5 or item['condition'] == 'Poor':
            return "This item should be recycled immediately to avoid environmental impact."
        elif item['age'] > 3 or item['condition'] == 'Good':
            return "Consider upgrading or recycling this item soon."
        elif item['condition'] == 'Excellent':
            return "This item is still in excellent condition, no immediate action required."
        else:
            return "Monitor this item regularly."
    
    def schedule_recycling(self, item):
        days_until_pickup = random.randint(1, 10)
        pickup_date = datetime.datetime.now() + datetime.timedelta(days=days_until_pickup)
        address = input("Enter your address for recycling pickup: ")
        phone_number = input("Enter your phone number: ")
        
        schedule_entry = {
            'item': item['name'],
            'pickup_date': pickup_date,
            'address': address,
            'phone_number': phone_number
        }
        self.schedule.append(schedule_entry)
        print(f"Recycling scheduled for {item['name']} in {days_until_pickup} days on {pickup_date.strftime('%Y-%m-%d')}.\n")

    def view_schedule(self):
        print("Recycling Pickup Schedule:\n")
        if not self.schedule:
            print("No recycling pickups scheduled.\n")
        else:
            for entry in self.schedule:
                print(f"Item: {entry['item']} | Pickup Date: {entry['pickup_date'].strftime('%Y-%m-%d')} | Address: {entry['address']} | Phone: {entry['phone_number']}\n")

    def generate_report(self):
        print("\nE-waste Monitoring System Report:\n")
        if not self.items and not self.schedule:
            print("No items or recycling scheduled in the system.\n")
        else:
            print("Monitored E-waste Items:")
            for item in self.items:
                print(f" - Name: {item['name']}, Category: {item['category']}, Age: {item['age']} years, Condition: {item['condition']}, Energy Consumption: {item['energy_consumption']} kWh, Added on: {item['added_date'].strftime('%Y-%m-%d')}")
            print("\nRecycling Pickup Schedule:")
            for entry in self.schedule:
                print(f" - Name: {entry['item']}, Pickup Date: {entry['pickup_date'].strftime('%Y-%m-%d')}, Address: {entry['address']}, Phone: {entry['phone_number']}")

def main():
    system = EWasteMonitoringSystem()

    while True:
        print("\nE-waste Monitoring System")
        print("1. Add an E-waste item")
        print("2. View recycling pickup schedule")
        print("3. Generate report")
        print("4. Exit\n")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name of the electronic item: ")
            category = input("Enter the category (e.g., Phone, Laptop, etc.): ")
            age = int(input("Enter the age of the item (in years): "))
            condition = input("Enter the condition (Excellent, Good, Poor): ")
            energy_consumption = float(input("Enter the energy consumption of the item (in kWh): "))
            system.add_item(name, category, age, condition, energy_consumption)
        
        elif choice == '2':
            system.view_schedule()
        
        elif choice == '3':
            system.generate_report()
        
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




