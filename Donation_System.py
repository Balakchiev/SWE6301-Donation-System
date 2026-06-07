class DonationSystem:
    def __init__(self):
        self.donations = []

    def add_donation(self, donor_name, amount):
        if not donor_name or donor_name.strip() == "":
            raise ValueError("Donor name is required")

        if amount <= 0:
            raise ValueError("Donation amount must be greater than zero")

        donation = {
            "donor_name": donor_name,
            "amount": amount
        }

        self.donations.append(donation)
        return donation

    def get_total_donations(self):
        return sum(donation["amount"] for donation in self.donations)

    def get_donation_count(self):
        return len(self.donations)