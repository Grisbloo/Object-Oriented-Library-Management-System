from datetime import datetime, timedelta

class LibraryMember:
    def __init__(self, name: str, expiry = datetime(2000, 1, 1)):
        self.name = name
        self.expiry = expiry
        self.standing = 100

    def is_in_good_standing(self) -> bool:
        return self.standing > 0

class LibraryItem:
    def __init__(self, name: str, due = datetime(2000, 1, 1)):
        self.name = name
        self.checked_out_by = ""
        self.due = due
        self.reservations = []

class Receipt:
    def __init__(self):
        self.error = ""
        self.items = []

    def add_item(self, lib_item: LibraryItem, due: datetime):
        self.items.append({ "name": lib_item.name, "due": due.strftime("%Y-%m-%d") })

    def __repr__(self):
        if self.error:
            return "Error: " + self.error
        return "Receipt: " + self.items.__repr__()

class Library:
    def __init__(self):
        self.items = {}
        self.now = datetime(2030, 1, 1)
    pass

    def increment_time(self, d: timedelta):
        self.now += d

    def print_now(self):
        print(f"Currently: {self.now.strftime("%Y-%m-%d")}")

    def add_item(self, lib_item: LibraryItem):
        self.items[lib_item.name] = lib_item

    def member_due_items(self, member: LibraryMember) -> list[str]:
        due_items = []
        for item in self.items:
            if item.checked_out_by == member.name:
                if self.now >= item.due:
                    due_items.append(item.name)
        return due_items

    def borrow_item(self, member: LibraryMember, item_names: list[str]):
        receipt = Receipt()
        #Holds can be taken from a borrow
        if not member.is_in_good_standing():
            receipt.error = "Not in Good Standing"
            return receipt

        if self.now >= member.expiry:
            receipt.error = "Member Expired"
            return receipt

        for item_name in item_names:
            if item_name not in self.items:
                continue

            checked_name = self.items[item_name].checked_out_by
            if checked_name:
                continue

            due_date = self.now + timedelta(days= 7)
            self.items[item_name].checked_out_by = member.name
            self.items[item_name].due = due_date

            receipt.add_item(self.items[item_name], due_date)
        return receipt


    def return_item(self, member: LibraryMember, item_names: list[str]):

        pass
        # def identify member(MemberID): **CheckedOutBy is member**
        # if Member is valid:
        #   bring up checkedoutby.member's receipt
        #   For checkedoutitem in receipt:
        #   Check due date and returndate (which is day of operation)
        #       If returned before due date, which is epirary date:
        #            do not convert loan to loanexpired
        #       else:
        #            returned after due date, convert loan to loanexpired
        #   convert checkedoutitem status to inlibrary
        #   Remove checkoutitem from reciept
        #   small waiting period before item becomes available to allow librarian to check items for damage/wear and tear
        #   Librarian approves for item to be availible to checkout


    def reserve_item(self, member: LibraryMember, item_names: list[str]):

        receipt = Receipt()

        if not member.is_in_good_standing():
            receipt.error = "Not in Good Standing"
            return receipt 

        if self.now >= member.expiry:
            receipt.error = "Member Expired"
            return receipt 
            
            for item_name in item_names:
                if item_name not in self.items:
                    continue

                item = self.items[item_name]

                # Precondition 4: Only allow reserve if no copies are available
                if not item.checked_out_by:
                    continue

                # Precondition 5: Prevent duplicate active reservations
                if member.name in item.reservations:
                    continue 

                # Postcondition: FIFO append and add to receipt
                item.reservations.append(member.name)
                receipt.add_item(item, item.due)

            return receipt

library = Library()
library.add_item(LibraryItem("The Great Gatsby"))
library.add_item(LibraryItem("Fahrenheit 451"))
library.add_item(LibraryItem("Spongebob's Big Adventure"))
library.add_item(LibraryItem("Peanuts Collection"))
library.add_item(LibraryItem("The Bible"))

library_member = LibraryMember("Joe", datetime(2030, 6, 1))

library.print_now()

r = library.borrow_item(library_member, ["The Great Gatsby", "The Bible"])

print(r)
print()

library.increment_time(timedelta(days= 31 * 6 - 5))

library.print_now()

r = library.borrow_item(library_member, ["Spongebob's Big Adventure"])

print(r)
