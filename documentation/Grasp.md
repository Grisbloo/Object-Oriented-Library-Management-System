## Controller 
### BorrowingController and ReservationController	
Handle system operations without placing application coordination logic inside the interface.
## Information Expert
### Loan.isOverdue()
A Loan has its due date and return date, making it the appropriate object to determine overdue status.
## Information Expert 
### ItemCopy.isAvailable()
Each copy maintains its own availability status.
## Creator 
### BorrowingController creates Loan objects; ReservationController creates Reservation objects.	
These controllers coordinate the corresponding transactions and have the information needed for creation.
## Low Coupling
### Separate borrowing and reservation controllers 
Reduces unnecessary dependencies between different operations.
## High Cohesion	
### Loan handles borrowing information while Reservation handles reservation information.
Each class focuses on a clearly defined responsibility.
## Indirection
### LibraryManagementSystem delegates operations to controllers.
Keeps external interface logic separate from transaction coordination.
