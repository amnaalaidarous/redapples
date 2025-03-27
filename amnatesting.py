from amnaclasses import Person, Guest, Room, Booking, Hotel, Payment, LoyaltyProgram, FeedbackReview, GuestServiceRequest

# Creating two Person objects
person1 = Person(1, "Ahmed Nasser", 32, "ahmed.nasser@luxuryhotels.ae", "General Manager")
person2 = Person(2, "Fatima Salem", 29, "fatima.salem@luxuryhotels.ae", "Front Desk Supervisor")

# Creating two Guest objects
guest1 = Guest(101, "Saeed Al Aidarous", 45, "saeed.al.aidarous@example.ae", "VIP Guest", 500, [])
guest2 = Guest(102, "Hind Al Aidarous", 38, "hind.al.aidarous@example.ae", "Regular Guest", 300, [])

# Creating two Room objects
room1 = Room(201, "Executive Suite", ["WiFi", "Smart TV", "Majlis-style seating", "Burj Khalifa View"], 1200, True)
room2 = Room(202, "Royal Suite", ["WiFi", "Private Pool", "Jacuzzi", "Sea View", "Butler Service"], 3500, True)

# Creating two Booking objects
booking1 = Booking(301, guest1, room1, "2025-10-15", "2025-10-20", 6000, True, True, True, 72, 5000)
booking2 = Booking(302, guest2, room2, "2025-12-05", "2025-12-10", 17500, False, True, False, 48, 8000)

# Creating two Hotel objects
hotel1 = Hotel("Emirates Grand Hotel", [room1], [guest1], [booking1])
hotel2 = Hotel("Palm Jumeirah Resort", [room2], [guest2], [booking2])

# Creating two Payment objects
payment1 = Payment(401, booking1, 6000, 500, "Dubai Islamic Bank Card", True, "Pending")
payment2 = Payment(402, booking2, 17500, 1000, "Apple Pay", True, "Processed")

# Creating two LoyaltyProgram objects
loyalty1 = LoyaltyProgram(501, guest1, 2000)
loyalty2 = LoyaltyProgram(502, guest2, 1500)

# Creating two FeedbackReview objects
review1 = FeedbackReview(601, guest1, hotel1, 5, "Unparalleled Emirati hospitality!", "2025-10-21")
review2 = FeedbackReview(602, guest2, hotel2, 4, "Amazing location and service, but breakfast could be better.", "2025-12-11")

# Creating two GuestServiceRequest objects
service_request1 = GuestServiceRequest(701, guest1, "Private Desert Safari Tour", "Pending")
service_request2 = GuestServiceRequest(702, guest2, "Late Check-out for Friday Prayer", "Approved")

# Welcome statement
print("Welcome to the Hotel Management System!\n")

# Printing the first person's related objects
print("---- First Person/Guest Details ----")
print(f"Person 1: {person1}")
print(f"Guest 1: {guest1}")
print(f"Room 1: {room1}")
print(f"Booking 1: {booking1}")
print(f"Hotel 1: {hotel1}")
print(f"Payment 1: {payment1}")
print(f"Loyalty 1: {loyalty1}")
print(f"Review 1: {review1}")
print(f"Service Request 1: {service_request1}\n")

# Printing the second person's related objects
print("---- Second Person/Guest Details ----")
print(f"Person 2: {person2}")
print(f"Guest 2: {guest2}")
print(f"Room 2: {room2}")
print(f"Booking 2: {booking2}")
print(f"Hotel 2: {hotel2}")
print(f"Payment 2: {payment2}")
print(f"Loyalty 2: {loyalty2}")
print(f"Review 2: {review2}")
print(f"Service Request 2: {service_request2}")
