from amnaclasses import Person, Guest, Room, Booking, Hotel, Payment, LoyaltyProgram, FeedbackReview, GuestServiceRequest


# Creating two Person objects
person1 = Person(1, "Alice Johnson", 28, "alice@example.com", "Manager")
person2 = Person(2, "Bob Smith", 35, "bob@example.com", "Receptionist")

# Creating two Guest objects
guest1 = Guest(101, "Charlie Brown", 40, "charlie@example.com", "Guest", 200, [])
guest2 = Guest(102, "Diana Ross", 33, "diana@example.com", "Guest", 150, [])

# Creating two Room objects
room1 = Room(201, "Deluxe", ["WiFi", "TV", "Mini-bar"], 150, True)
room2 = Room(202, "Suite", ["WiFi", "Jacuzzi", "Ocean View"], 300, True)

# Creating two Booking objects
booking1 = Booking(301, guest1, room1, "2025-04-01", "2025-04-05", 600)
booking2 = Booking(302, guest2, room2, "2025-05-10", "2025-05-15", 1500)

# Creating two Hotel objects
hotel1 = Hotel("Grand Palace", [room1], [guest1], [booking1])
hotel2 = Hotel("Ocean Breeze", [room2], [guest2], [booking2])

# Creating two Payment objects
payment1 = Payment(401, booking1, 600, "Credit Card", "Pending")
payment2 = Payment(402, booking2, 1500, "PayPal", "Processed")

# Creating two LoyaltyProgram objects
loyalty1 = LoyaltyProgram(501, guest1, 200)
loyalty2 = LoyaltyProgram(502, guest2, 150)

# Creating two FeedbackReview objects
review1 = FeedbackReview(601, guest1, hotel1, 5, "Excellent stay!", "2025-04-06")
review2 = FeedbackReview(602, guest2, hotel2, 4, "Great service, but noisy.", "2025-05-16")

# Creating two GuestServiceRequest objects
service_request1 = GuestServiceRequest(701, guest1, "Room Cleaning", "Pending")
service_request2 = GuestServiceRequest(702, guest2, "Late Check-out", "Approved")

# Welcome statement
print("Welcome to the Hotel Management System!\n")

# Printing the first person's related objects
print("---- First Person Details ----")
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
print("---- Second Person Details ----")
print(f"Person 2: {person2}")
print(f"Guest 2: {guest2}")
print(f"Room 2: {room2}")
print(f"Booking 2: {booking2}")
print(f"Hotel 2: {hotel2}")
print(f"Payment 2: {payment2}")
print(f"Loyalty 2: {loyalty2}")
print(f"Review 2: {review2}")
print(f"Service Request 2: {service_request2}")

