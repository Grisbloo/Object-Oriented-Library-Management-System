# OC-01: Confirm Borrowing
## Borrow Item

Operation: confirmBorrowing()

Cross-reference: Borrow Item use case

Preconditions:
1. The librarian has identified an existing library member.
2. The member's account is active and in good standing.
3. At least one ItemCopy has been scanned and selected for borrowing.
4. Every selected copy exists and is available to the member.
5. Each selected copy has no active loan.
6. The member has not exceeded any applicable borrowing limits.
Postconditions (on successful completion):
1. A new Loan instance was created for each selected ItemCopy.
2. Each new Loan was associated with the borrowing LibraryMember.
3. Each new Loan was associated with its corresponding ItemCopy.
4. The checkoutDate attribute of each new Loan was assigned the current date.
5. The dueDate attribute of each new Loan was assigned according to library borrowing policy.
6. The returnDate of each new Loan was initialized to null.
7. The availabilityStatus of each borrowed ItemCopy was changed to Borrowed.
8. Each new Loan became part of the member's borrowing records.

# OC-02: Confirm Returns
## Return Item

Operation: confirmReturns()

Cross-reference: Return Item use case

Preconditions:
1. The librarian has identified an existing member.
2. At least one ItemCopy has been scanned and selected for return.
3. Every selected copy exists in the library system.
4. Each selected copy is associated with an active Loan belonging to the identified member.
5. None of the selected loans has already been closed.
Postconditions (on successful completion):
1. The returnDate attribute of each associated Loan was assigned the current date.
2. Each returned copy's associated Loan was marked as completed.
3. Each completed Loan was no longer considered an active borrowing transaction.
4. Each completed Loan remained associated with the member for borrowing-history purposes.
5. For each returned ItemCopy without a pending reservation, its availabilityStatus was changed to Available.
6. For each returned copy whose LibraryItem had an eligible pending reservation:
   - The highest-priority eligible Reservation was selected.
   - The returned ItemCopy was associated with that reservation.
   - The copy's availabilityStatus was changed to OnHold.
   - The reservation's status was updated to ReadyForPickup.
7. The member's collection of active loans no longer included the completed transactions.

# OC-03: Request Reservation
## Reserve Item

Operation: requestReservation(memberId, itemId)

Cross-reference: Reserve Item use case

Preconditions:
1. The LibraryMember identified by memberId exists.
2. The member's account is active and in good standing.
3. The LibraryItem identified by itemId exists in the catalog.
4. No copies of the selected item are currently available for ordinary borrowing.
5. The member does not already have an active reservation for the selected item.
Postconditions (on successful completion):
1. A new Reservation instance was created.
2. The new Reservation was associated with the requesting LibraryMember.
3. The new Reservation was associated with the selected LibraryItem.
4. The reservationDate attribute was assigned the current date.
5. The status attribute was initialized to Pending.
6. The reservation was placed after all existing pending reservations for the same item, preserving FIFO priority.
7. The new reservation became part of the member's reservation records.
8. The reservation received a unique reservationId.
