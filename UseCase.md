# Use Cases

## Borrow Item
### Primary actor(s)
- Library Member
- Librarian
### Preconditions
- The person attempting to checkout a book has a library card and is in good standing.
- The item that is being attempted to checkout exists on the library database.
- The item is not reserved.
- The librarian is able to log on to the system.
### Main Success Scenario
1. The member scans their library card.
2. The account is succesfully pulled up and is in good standing.
3. The item is scanned.
4. The item is verified to be available.
5. The item is checked out to the member.
6. Steps 3-5 are repeated for all items.
7. A receipt is printed with all relevant information i.e. items and due dates
### Appropriate Alternative/Exception Flows
- A member's library card is expired
    - If the member proceeds with renewing their membership, then the scenario continues on step 3.
- An item is reserved
    - The librarian to set it aside and continue with the rest of the items.
### Postconditions
-  Each item is successfully marked as checked out in the system.

## Return Item
### Primary actor(s)
- Member
- Librarian
### Preconditions
- The item is currently checked out and linked to the member's library card.
- The Librarian is able to log on to the system.
### Main Success Scenario
1. The Librarian scans the member's library card
2. The Librarian scans the item. 
3. The system removes the item from the member's account.
4. The system marks the item as available.
5. Steps 2-4 are repeated for all items.
6. A receipt is printed with a summary of all returned items

### Appropriate Alternative/Exception Flows
- The barcode is unscannable
    - The librarian manually types the barcode in to the computer.
- The item is damaged
    - The member is charged a fee.
- The item has a pending reservation
    - The item is placed On Hold rather than as Available.
### Postconditions
-  The item's current status is successfully updated and the member no longer has the item on their account.
## Reserve Item

### Primary actor(s)
- Member
### Preconditions
- The person attempting to checkout a book has a library card and is in good standing.
- The item that is being attempted to reserve exists on the library database.
- The item is not available.
### Main Success Scenario
1. The member searches the catalog and selects the item they want.
2. The system displays the item and shows there is no available copies.
3. The member selects reserve.
4. The system confirms the member's account is in good standing.
5. The item is successfully reserved.
### Appropriate Alternative/Exception Flows
- The item is available
    - The member is prompted to Borrow Item.
- A member's library card is expired
    - If the member proceeds with renewing their membership. Then the scenario can begin at step 1.
- Another member already has a reservation set.
    - This reservation is created with the prior one(s) having priority.
### Postconditions
- The reservation is succesfully created

## Register Member
### Primary actor(s)
- Librarian
- Guest
### Preconditions
- The person register to become a member is a Guest and not an existing Member. 
- The librarian has permissions to create a new account.
- The system is operational.
### Main Success Scenario
1. The person asks to register to become a library member.
2. The librarian searches the system for the person's information.
3. The system finds no matching record.
5. The librarian examines the person's identification and proof of address and marks them as verified.
6. The system validates inputs in all required fields.
7. The system creates the member account with a unique member ID.
8. The librarian scans a blank library card and links the card to the new account.
9. The librarian hands the library card to the new member.
### Appropriate Alternative/Exception Flows
-
### Postconditions
-  A new member account is created with a Unique ID and the account is able to borrow/return items.

## Manage Member

### Primary actor(s)
- Librarian

### Preconditions
- The librarian is able to log on to the system.
- The librarian has permission to manage member accounts.
- The member being managed already exists in the library database.

### Main Success Scenario
1. The librarian logs into the library management system.
2. The librarian searches for a member using their library card or member ID.
3. The system retrieves the member's account information.
4. The librarian selects the member account they wish to manage.
5. The system displays the member's information, membership status, and borrowing history.
6. The librarian selects the information or account status they wish to modify.
7. The librarian enters the updated information.
8. The system validates the updated information.
9. The system saves the changes to the member's account.
10. The system displays a confirmation that the member's account has been successfully updated.

### Appropriate Alternative/Exception Flows
- The member cannot be found.
    - The system informs the librarian that no matching member exists.
    - The librarian may search again or proceed to Register Member.
- The updated information is invalid or incomplete.
    - The system displays an error explaining which information is invalid.
    - The librarian corrects the information and continues from step 7.
- The member's account is expired.
    - The librarian may renew the membership if the member meets the renewal requirements.
- The member has outstanding loans or reservations.
    - The system prevents account deactivation if unresolved borrowing or reservation activity would violate library policy.

### Postconditions
- The member's account information is successfully updated in the system.
- The updated membership information is available for future borrowing, returning, and reservation operations.
- The member's existing borrowing history is preserved.

## Manage Reservations

### Primary actor(s)
- Librarian

### Preconditions
- The librarian is able to log on to the system.
- The librarian has permission to manage reservations.
- The library database contains reservation information.
- The reservation being managed exists in the system.

### Main Success Scenario
1. The librarian logs into the library management system.
2. The librarian accesses the reservation management section.
3. The system displays the outstanding reservations.
4. The librarian selects a reservation to manage.
5. The system displays the reservation details, including the requesting member, reserved item, reservation date, and current status.
6. The librarian reviews the reservation and determines whether the requested item has an available copy.
7. The system verifies the reservation's priority relative to other outstanding reservations for the same item.
8. If an eligible reservation has priority and a copy is available, the librarian selects the option to fulfill the reservation.
9. The system assigns the available copy to the reservation and marks it as On Hold.
10. The system updates the reservation status and displays confirmation of the changes.

### Appropriate Alternative/Exception Flows
- No reservations exist.
    - The system informs the librarian that there are no outstanding reservations.
- The requested item is unavailable.
    - The reservation remains active until an eligible copy becomes available.
- Multiple members have reserved the same item.
    - The system prioritizes reservations based on the order in which they were created.
    - Later reservations remain pending until their turn is reached.
- The requesting member is no longer eligible.
    - The system prevents the reservation from being fulfilled.
    - The librarian may cancel the reservation according to library policy.
- The member requests cancellation.
    - The librarian selects the reservation and chooses Cancel Reservation.
    - The system updates the reservation status to Cancelled.
    - Any copy held exclusively for the cancelled reservation is released or assigned to the next eligible reservation.
- The reservation has already been fulfilled or cancelled.
    - The system prevents the librarian from fulfilling or cancelling the reservation again.

### Postconditions
- The selected reservation is updated appropriately.
- Fulfilled reservations are associated with an available copy placed On Hold.
- Cancelled reservations are no longer considered active.
- Outstanding reservations retain their correct priority.
- The availability of affected library copies is updated accordingly.
