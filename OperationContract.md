# OC-01: Confirm Borrowing
## Borrow Item

Operation: `confirmBorrowing()`

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

Operation: `confirmReturns()`

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

Operation: `requestReservation(memberId, itemId)`

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

# OC-04: Register Member
## Register Member

Operation: `registerMember(memberInformation, cardId)`

Cross-reference: Register Member use case

Preconditions:
1. The librarian is authenticated and authorized to register new members.
2. The applicant does not already have an existing membership.
3. The applicant's identification and proof of address have been verified.
4. All required registration information has been provided.
5. The library card identified by cardId exists and is unassigned.  

Postconditions (on successful completion):
1. A new LibraryMember instance was created.
2. The new member was assigned a unique memberId.
3. The member's personal and contact information was recorded.
4. The member's membership status was initialized to Active.
5. The member's registration date was assigned the current date.
6. The selected library card was associated with the new member.
7. The library card was marked as assigned.
8. The new member became eligible to borrow and reserve items according to library policy.

# OC-05: Update Member
## Manage Member

Operation: `updateMember(memberId, updatedInformation)`

Cross-reference: Manage Member use case

Preconditions:
1. The librarian is authenticated and authorized to manage members.
2. The LibraryMember identified by memberId exists.
3. The requested updates comply with library membership policies.
4. The submitted information is valid and complete.
5. Any requested account deactivation satisfies outstanding loan and reservation restrictions.  

Postconditions (on successful completion):
1. The specified attributes of the existing LibraryMember were updated.
2. Any requested and permitted membership status change was recorded.
3. The member's unique memberId remained unchanged.
4. The member's existing Loan and Reservation associations were preserved unless an authorized operation explicitly changed them.
5. The member's borrowing history was preserved.
6. The updated member information became available to subsequent library operations.

# OC-06: Fulfill Reservation
## Manage Reservations

Operation: `fulfillReservation(reservationId, copyId)`

Cross-reference: Manage Reservations use case

Preconditions:
1. The librarian is authenticated and authorized to manage reservations.
2. The Reservation identified by reservationId exists and has status Pending.
3. The requesting LibraryMember remains eligible.
4. The ItemCopy identified by copyId exists and is Available.
5. The copy belongs to the LibraryItem associated with the reservation.
6. The reservation has the highest eligible priority among pending reservations for that item.  

Postconditions (on successful completion):
1. The selected ItemCopy was associated with the reservation.
2. The copy's availabilityStatus was changed to OnHold.
3. The reservation's status was changed to ReadyForPickup.
4. The reservation retained its association with the requesting member.
5. The reservation retained its association with the requested library item.
6. The copy was no longer available for ordinary borrowing.
7. Other pending reservations retained their relative priority.
8. The updated reservation and copy states were saved.

# OC-07: Cancel Reservation
## Manage Reservations

Operation: `cancelReservation(reservationId)`

Cross-reference: Manage Reservations use case

Preconditions:
1. The librarian is authenticated and authorized to manage reservations.
2. The specified Reservation exists.
3. The reservation is currently Pending or ReadyForPickup.
4. The reservation has not already been cancelled or fulfilled.  

Postconditions (on successful completion):
1. The reservation's status was changed to Cancelled.
2. The reservation was removed from active reservation processing.
3. If an ItemCopy was held exclusively for the reservation, that hold was released.
4. If another eligible reservation was waiting for the same LibraryItem, the released copy was assigned to the highest-priority eligible reservation.
5. Otherwise, the released copy's availabilityStatus was changed to Available.
6. Any remaining pending reservations retained their relative FIFO priority.
7. The cancelled reservation remained in the member's reservation history.
