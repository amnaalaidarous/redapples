
# The Person class represents a person with essential details.
class Person:
    def __init__(self, person_id, name, age, contact_info, role):
        # Initializes the attributes of a person
        self.person_id = person_id
        self.name = name
        self.age = age
        self.contact_info = contact_info
        self.role = role

    # Setter and getter methods for each attribute
    def setPersonID(self, person_id):
        self.person_id = person_id

    def getPersonID(self):
        return self.person_id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setContactInfo(self, contact_info):
        self.contact_info = contact_info

    def getContactInfo(self):
        return self.contact_info

    def setRole(self, role):
        self.role = role

    def getRole(self):
        return self.role

    # String representation of the Person object
    def __str__(self):
        return f"Person[ID={self.person_id}, Name={self.name}, Age={self.age}, Contact Information= {self.contact_info}, Role={self.role}]"

# The Guest class inherits from Person and represents a guest with added loyalty points and reservation history.
class Guest(Person):
    def __init__(self, person_id, name, age, contact_info, role, loyalty_points, reservation_history):
        super().__init__(person_id, name, age, contact_info, role)
        # Additional attributes for Guest
        self.loyalty_points = loyalty_points
        self.reservation_history = reservation_history

    # Setter and getter methods for the new attributes
    def setLoyaltyPoints(self, points):
        self.loyalty_points = points

    def getLoyaltyPoints(self):
        return self.loyalty_points

    def setReservationHistory(self, reservation_history):
        self.reservation_history = reservation_history

    def getReservationHistory(self):
        return self.reservation_history

    # Method to add a booking to the reservation history
    def addBooking(self, booking):
        self.reservation_history.append(booking)

    # String representation of the Guest object
    def __str__(self):
        return (f"Guest[ID={self.person_id}, Name={self.name}, Age={self.age}, Contact={self.contact_info}, "
                f"Role={self.role}, Loyalty Points={self.loyalty_points}, "
                f"Reservations={[booking.getBookingID() for booking in self.reservation_history]}]")

# The Hotel class represents a hotel with rooms, guests, and bookings.
class Hotel:
    def __init__(self, hotel_name, rooms, guests, bookings):
        # Initializes hotel details
        self.hotel_name = hotel_name
        self.rooms = rooms
        self.guests = guests
        self.bookings = bookings

    # Setter and getter methods for hotel attributes
    def setHotelName(self, hotel_name):
        self.hotel_name = hotel_name

    def getHotelName(self):
        return self.hotel_name

    def addRoom(self, room):
        self.rooms.append(room)

    def getRooms(self):
        return self.rooms

    def addGuest(self, guest):
        self.guests.append(guest)

    def getGuests(self):
        return self.guests

    def addBooking(self, booking):
        self.bookings.append(booking)

    def getBookings(self):
        return self.bookings

    # String representation of the Hotel object
    def __str__(self):
        return (f"Hotel[Name={self.hotel_name}, Rooms={len(self.rooms)}, Guests={len(self.guests)}, "
                f"Bookings={len(self.bookings)}]")

# The Room class represents a room in a hotel with amenities, price, and availability status.
class Room:
    def __init__(self, room_number, room_type, amenities, price_per_night, availability_status):
        # Initializes room details
        self.room_number = room_number
        self.room_type = room_type
        self.amenities = amenities
        self.price_per_night = price_per_night
        self.availability_status = availability_status

    # Setter and getter methods for room attributes
    def setRoomNumber(self, room_number):
        self.room_number = room_number

    def getRoomNumber(self):
        return self.room_number

    def setRoomType(self, room_type):
        self.room_type = room_type

    def getRoomType(self):
        return self.room_type

    def setAmenities(self, amenities):
        self.amenities = amenities

    def getAmenities(self):
        return self.amenities

    def setPricePerNight(self, price):
        self.price_per_night = price

    def getPricePerNight(self):
        return self.price_per_night

    def isAvailable(self):
        return self.availability_status

    def setAvailability(self, status):
        self.availability_status = status

    # String representation of the Room object
    def __str__(self):
        return (f"Room[Number={self.room_number}, Type={self.room_type}, "
                f"Amenities={self.amenities}, Price={self.price_per_night}, "
                f"Availability Status={self.availability_status}]")

# The Booking class represents a booking made by a guest in a room.
class Booking:
    def __init__(self, booking_id, guest, room, check_in_date, check_out_date, confirm_notification, access_invoice, cancel_booking, update_availability, cancel_notice, total_amount):
        # Initializes booking details
        self.booking_id = booking_id
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.confirm_notification = confirm_notification
        self.access_invoice = access_invoice
        self.cancel_booking = cancel_booking
        self.update_availability = update_availability
        self.cancel_notice = cancel_notice
        self.total_amount = total_amount

    # Setter and getter methods for booking attributes
    def setBookingID(self, booking_id):
        self.booking_id = booking_id

    def getBookingID(self):
        return self.booking_id

    def setGuest(self, guest):
        self.guest = guest

    def getGuest(self):
        return self.guest

    def setRoom(self, room):
        self.room = room

    def getRoom(self):
        return self.room

    def setCheckInDate(self, date):
        self.check_in_date = date

    def getCheckInDate(self):
        return self.check_in_date

    def setCheckOutDate(self, date):
        self.check_out_date = date

    def getCheckOutDate(self):
        return self.check_out_date

    def setConfirmNotification(self, confirm_notification):
        self.confirm_notification = confirm_notification

    def getConfirmNotification(self):
        return self.confirm_notification

    def setAccessInvoice(self, access_invoice):
        self.access_invoice = access_invoice

    def getAccessInvoice(self):
        return self.access_invoice

    def setBookingCancellation(self, cancel_booking):
        self.cancel_booking = cancel_booking

    def getBookingCancellation(self):
        return self.cancel_booking

    def setUpdateAvailability(self, update_availability):
        self.update_availability = update_availability

    def getUpdateAvailability(self):
        return self.update_availability

    def setCancelNotice(self, cancel_notice):
        self.cancel_notice = cancel_notice

    def getCancelNotice(self):
        return self.cancel_notice

    # Calculate the total booking amount
    def calculateTotalAmount(self):
        return self.total_amount

    # String representation of the Booking object
    def __str__(self):
        return (f"Booking[ID={self.booking_id}, Guest={self.guest.name}, Room={self.room.room_number}, "
                f"Check-in={self.check_in_date}, Check-out={self.check_out_date}, Confirm Notification={self.confirm_notification}, "
                f"Access Invoice={self.access_invoice}, Cancel Booking={self.cancel_booking}, Update Availability={self.update_availability}, "
                f"Cancel Notice={self.cancel_notice}, Total={self.total_amount}]")


# The Payment class represents a payment for a booking.
class Payment:
    def __init__(self, payment_id, booking, amount, charges_and_discounts, payment_method, invoice_generation, status):
        # Initializes payment details
        self.payment_id = payment_id
        self.booking = booking
        self.amount = amount
        self.charges_and_discounts = charges_and_discounts
        self.payment_method = payment_method
        self.invoice_generation = invoice_generation
        self.status = status

    # Setter and getter methods for payment attributes
    def setPaymentID(self, payment_id):
        self.payment_id = payment_id

    def getPaymentID(self):
        return self.payment_id

    def setBooking(self, booking):
        self.booking = booking

    def getBooking(self):
        return self.booking

    def setAmount(self, amount):
        self.amount = amount

    def getAmount(self):
        return self.amount

    def setChargesAndDiscounts(self, charges_and_discounts):
        self.charges_and_discounts = charges_and_discounts

    def getChargesAndDiscounts(self):
        return self.charges_and_discounts

    def setPaymentMethod(self, method):
        self.payment_method = method

    def getPaymentMethod(self):
        return self.payment_method

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status

    def setInvoiceGeneration(self, invoice_generation):
        self.invoice_generation = invoice_generation

    def getInvoiceGeneration(self):
        return self.invoice_generation

    # Method to process payment status
    def processPayment(self):
        self.status = "Processed"

    # String representation of the Payment object
    def __str__(self):
        return (f"Payment[ID={self.payment_id}, BookingID={self.booking.booking_id}, Amount={self.amount}, "
                f"ChargesAndDiscounts={self.charges_and_discounts}, Method={self.payment_method}, "
                f"InvoiceGeneration={self.invoice_generation}, Status={self.status}]")


# The LoyaltyProgram class represents the loyalty program a guest can participate in.
class LoyaltyProgram:
    def __init__(self, program_id: int, guest: Guest, points: int):
        # Initializes loyalty program details
        self.program_id = program_id
        self.guest = guest
        self.points = points
        self.rewards = []

    # Setter and getter methods for loyalty program attributes
    def setProgramID(self, program_id):
        self.program_id = program_id

    def getProgramID(self):
        return self.program_id

    def setGuest(self, guest):
        self.guest = guest

    def getGuest(self):
        return self.guest

    def setPoints(self, points):
        self.points = points

    def getPoints(self):
        return self.points

    # Method to add points to the guest's loyalty program
    def addPoints(self, points):
        self.points += points

    # Method to redeem rewards
    def redeemReward(self, reward):
        if reward in self.rewards:
            self.rewards.remove(reward)
            return True
        return False

    # Getter for rewards
    def getRewards(self) -> list[str]:
        return self.rewards

    # String representation of the LoyaltyProgram object
    def __str__(self):
        return (f"LoyaltyProgram[ID={self.program_id}, Guest={self.guest.name}, "
                f"Points={self.points}, Rewards={self.rewards}]")

# The FeedbackReview class represents a guest's feedback and review for a hotel stay.
class FeedbackReview:
    def __init__(self, review_id, guest, hotel, rating, comments, review_date):
        # Initializes the feedback review details
        self.review_id = review_id
        self.guest = guest
        self.hotel = hotel
        self.rating = rating
        self.comments = comments
        self.review_date = review_date

    # Setter and getter methods for the review attributes
    def setReviewID(self, review_id):
        self.review_id = review_id

    def getReviewID(self):
        return self.review_id

    def setGuest(self, guest):
        self.guest = guest

    def getGuest(self):
        return self.guest

    def setHotel(self, hotel):
        self.hotel = hotel

    def getHotel(self):
        return self.hotel

    def setRating(self, rating):
        self.rating = rating

    def getRating(self):
        return self.rating

    def setComments(self, comments):
        self.comments = comments

    def getComments(self):
        return self.comments

    def setReviewDate(self, review_date):
        self.review_date = review_date

    def getReviewDate(self):
        return self.review_date

    # String representation of the FeedbackReview object
    def __str__(self):
        return (f"FeedbackReview[ID={self.review_id}, Guest={self.guest.name}, "
                f"Hotel={self.hotel.hotel_name}, Rating={self.rating}, "
                f"Comments={self.comments}, Date={self.review_date}]")

# The GuestServiceRequest class represents a request made by a guest for a specific service at the hotel.
class GuestServiceRequest:
    def __init__(self, request_id, guest, service_type, status):
        # Initializes the guest service request details
        self.request_id = request_id
        self.guest = guest
        self.service_type = service_type
        self.status = status

    # Setter and getter methods for the service request attributes
    def setRequestId(self, request_id):
        self.request_id = request_id

    def getRequestId(self):
        return self.request_id

    def setGuest(self, guest):
        self.guest = guest

    def getGuest(self):
        return self.guest

    def setServiceType(self, service_type):
        self.service_type = service_type

    def getServiceType(self):
        return self.service_type

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status

    # Method to update the status of the service request
    def updateStatus(self, status):
        self.status = status

    # String representation of the GuestServiceRequest object
    def __str__(self):
        return (f"GuestServiceRequest[ID={self.request_id}, Guest={self.guest.name}, "
                f"Service Type={self.service_type}, Status={self.status}]")
