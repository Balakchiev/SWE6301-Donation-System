from Donation_System import DonationSystem

system = DonationSystem()

try:
    system.add_donation("Mario", 50)
    system.add_donation("Yosif", 20)

    print("Donation system running successfully")
    print(f"Total Donations Received: £{system.get_total_donations()}")
    print(f"Total Number of Donations: {system.get_donation_count()}")

except ValueError as error:
    print(f"Error: {error}")