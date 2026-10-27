# Assumptions
The system maintains library members, catalog items, physical copies, loans, and reservations.

Multiple physical copies may belong to one library item.

Each physical copy may have many historical loans but no more than one active loan.

A library member may have multiple active loans and reservations.

Reservations are associated with a library item rather than a specific physical copy until fulfillment.

Reservations are fulfilled according to FIFO priority among eligible members.

Members cannot create duplicate active reservations for the same item.

Item-copy availability statuses include Available, Borrowed, and OnHold.

The system preserves completed loans as borrowing history.

Borrowing and returning are processed as transactions, so validation failures do not leave partially updated records.
