from datetime import datetime

class LibraryMember:
    def __init__(self, name: str, expiry: datetime):
        self.name = name
        self.expiry = expiry
        self.in_good_standing = True

    def is_in_good_standing(self):
        return self.in_good_standing

class LibraryItem:
    def __init__(self, name: str, due = datetime(2000, 1, 1)):
        self.name = name
        self.checked_out_by = ""
        self.due = due
        self.reservations = []

class Receipt:
    def __init__(self):
        self.item_due_map = {}
        self.error = ""

    def add_item(self, item: LibraryItem, due: datetime):
        self.item_due_map[item.name] = due

    def __str__(self):
        receipt_str = ""
        for name in self.item_due_map:
            receipt_str += f"{name} : {self.item_due_map[name]}\n"
        if self.error:
            receipt_str += f"Error: {self.error}\n"
        return receipt_str

class Library:
    def __init__(self, now = datetime(2025, 1, 1)):
        self.items: dict[str, LibraryItem] = {}
        self.now = now

    def add_item(self, lib_item: LibraryItem):
        self.items[lib_item.name] = lib_item

    def borrow_item(self, member: LibraryMember, item_names: list[str]):
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

            if item.checked_out_by:
                continue

            receipt.add_item(item, self.now)
            item.checked_out_by = member.name

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

    def cancel_reservation(self, member: LibraryMember, item_name: str) -> bool:
        if item_name not in self.items:
            return False

        item = self.items[item_name]

        # Precondition: Member must have an active reservation in queue or held
        if member.name in item.reservations:
            item.reservations.remove(member.name)
            return True

        # Postcondition: If item was actively held for this member, pass to next or make available
        if item.checked_out_by == f"HOLD:{member.name}":
            if item.reservations:
                next_member = item.reservations.pop(0)
                item.checked_out_by = f"HOLD:{next_member}"
            else:
                item.checked_out_by = ""
            return True

        return False

    def fulfill_reservation(self, item_name: str) -> str:
        if item_name not in self.items:
            return "Item not found"

        item = self.items[item_name]

        # Precondition 3: An available copy must exist (not currently borrowed or held)
        if item.checked_out_by != "":
            return "No available copy to fulfill reservation"

        # Precondition 2: There must be at least one pending reservation
        if not item.reservations:
            return "No pending reservations for this item"

        # Postcondition: Assign available copy to highest-priority waiting patron (FIFO)
        next_member = item.reservations.pop(0)
        item.checked_out_by = f"HOLD:{next_member}"
        return f"Reservation fulfilled: copy placed on hold for {next_member}"

library = Library()
library.add_item(LibraryItem("The Great Gatsby"))
library.add_item(LibraryItem("Fahrenheit 451"))
library.add_item(LibraryItem("Spongebob's Big Adventure"))
library.add_item(LibraryItem("Peanuts Collection"))

library_member = LibraryMember("Joe", datetime(2026, 1, 1))

receipt = library.borrow_item(library_member, ["The Great Gatsby", "Peanuts Collection"])
print(receipt)
