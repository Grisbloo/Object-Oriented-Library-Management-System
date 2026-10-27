## Borrow Item
### Class	Responsibility
LibraryManagementSystem - Receives system events from the librarian.  
BorrowingController	- Coordinates and validates the borrowing transaction.  
LibraryMember	- Provides membership status and current borrowing information.  
LibraryCatalog -	Locates requested physical copies.  
ItemCopy -	Reports and updates its availability.  
LoanPolicy -	Determines eligibility and due dates.  
Loan -	Records borrowing details and maintains the transaction.  

### Collaboration:
1. The librarian submits the borrowing request through LibraryManagementSystem.
2. The system delegates the request to BorrowingController.
3. The controller retrieves the member and requested copies.
4. The member and loan policy provide the information needed to determine eligibility.
5. The controller verifies that the copies can be borrowed.
6. A Loan is created for each borrowed copy.
7. The loans are associated with the member and their corresponding copies.
8. The copies' statuses are updated to Borrowed.
9. A confirmation containing the assigned due dates is returned.

## Return Item
### Class	Responsibility
LibraryManagementSystem - Receives the return request.  
BorrowingController -	Coordinates the return transaction.  
Loan -	Records the return date and determines overdue status.  
ItemCopy -	Updates its availability.  
ReservationController -	Determines whether a pending reservation should receive the returned copy.  
Reservation -	Maintains the resulting reservation status.  

### Collaboration:
1. The librarian submits the return request.
2. BorrowingController locates the active loan associated with each returned copy.
3. The controller verifies that the loan belongs to the identified member.
4. The Loan records its return date.
5. ReservationController checks for pending reservations associated with the returned copy's LibraryItem.
6. If an eligible reservation exists, the copy is assigned to that reservation and marked OnHold.
7. Otherwise, the copy is marked Available.
8. The completed loan remains in the member's borrowing history.
9. The system returns a summary of the transaction.
    
## Reserve Item
### Class	Responsibility
LibraryManagementSystem -	Receives the reservation request.  
ReservationController -	Validates and coordinates the reservation.  
LibraryMember -	Provides membership eligibility information.  
LibraryCatalog -	Retrieves the selected item and its copies.  
LibraryItem -	Provides information about available copies.  
Reservation -	Records the reservation and its current status.  

### Collaboration:
1. The member selects an unavailable item and requests a reservation.
2. LibraryManagementSystem forwards the request to ReservationController.
3. The controller retrieves the member and selected catalog item.
4. The controller verifies membership eligibility.
5. The controller confirms that no copies are available for ordinary borrowing.
6. The controller checks for an existing active reservation by the same member.
7. A new Reservation is created.
8. The reservation is associated with the member and library item.
9. The reservation is placed at the end of the existing FIFO queue.
10. The system returns confirmation and the member's queue position.
