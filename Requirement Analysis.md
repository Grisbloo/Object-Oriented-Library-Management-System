# Requirements Analysis
For this specific task it is required that we find the  
• functional requirements;  
• relevant non-functional requirements;  
• system actors;  
• major system functionality  

I broke this up into its 4 components:
## Functional Requirements
### Catalog Management
The system shall maintain a collection of library items
The system shall support multiple types of library items including:
- Books  
- Audiobooks  
- DVDs  
- Movies  
- Games  
- Other resources

The system shall maintain descriptive information for each library item, including:
- Title
- Author/Creator
- Item Type
- Unique ID
- Current availability

The system shall support multiple physical copies of the same library item  
The system shall allow users to browse the library catalog  
The system shall allow users to search the catalog by the available descriptors including:  
- Title
- Author/Creator
- Item Type
- Unique ID
- Current availability  

### Member management
The system shall maintain information about registered library members  
The system shall allow members to view the items they currently have borrowed  
The system shall allow members to view relevant information about their borrowing activity  

### Borrowing and returning
The system shall allow a member to borrow an available library item  
The system shall record each borrowing transation  
The system shall assign and appropriate due date to borrowed items  
The system shall prevent invalid borrowing operations  
The systems shall allow a member to return an item they have borrowed  
The system shall update the items availability when an item is reuturned  
The system shall determine whether a borrowed item is overdue  

### Reservations
The system shall allow a member to reserve an unavailable item  
The system shall maintain information about outstanding reservations  
The system shall handle a reservation when the reserved item becomes available  

### Library Resource Management
The system shall allow librarians to manage library resources  
The system shall allow librarians to perform member-related operations  
  
## Relevant non-functional requirements
- Usability: The system should provide a straightforward interface for browsing, searching, borrowing, reuturning and reserving library items  
- Reliability: The system should maintain accurate borrowing, returning, availability and reservation information  
- Data Integrity: The system should prevent inconsistent states such as an item simultaneously being recorded as available and borrowed  
- Security: Only authorized users should be able to perform operations appropriate to their role  
- Maintainability: The system should be designed so that additional library item types can be added without requiring substantial changes to existing functionality  
- Extendibility: The system should support multiple copies of library items and additional resource types as the library's catalog grows  
- Performance: Catalog searches and common library operations should complete within a reasonable amount of time  
The system should remain accessible during normal library operating periods  
  
## System actors
### Library Member
- Searches and browses the catalog
- Views borrowed items and borrowing history
- Borrows available items
- Returns borrowed items
- Reserves unavailable items
### Guest
- Browses and searches the library catalog
- May view item availability
- Cannot perform member-only operations such as borrowing or reserving items
### Librarian
- Manages library resources
- Performs member-related operations
- May assist with borrowing, returning, and reservation operations
### Database Manager
- Maintains and manages the system's underlying library data
- Ensures that catalog, member, borrowing, and reservation information is properly maintained
### IT/System Administrator
- Maintains the technical operation of the system
- Manages system configuration, access, and technical issues
  
## Major System functionality
Manage Library Catalog
- Add, modify, remove, and maintain library resources and their copies

Browse and Search Catalog
- Allow users to locate library items using available descriptors

Manage Library Members
- Maintain registered member information and member activity

Borrow Library Item
- Allow members to borrow available items and create borrowing transactions

Return Library Item
- Process returns and update item availability

Track Borrowing Activity
- Maintain borrowing records, due dates, and overdue status

Reserve Library Item
- Allow members to reserve currently unavailable items

Manage Reservations
- Maintain outstanding reservations and process reservations when items become available

## Assumptions
- Database management and technical administration are considered external supporting roles even though they are not explicitly described in the project specification (and are probably needed for maintenance
- The system distinguishes between a library item/title and individual physical copies
- Each individual copy has a unique identifier
- A member must be registered before borrowing or reserving items
- An item must be available before it can be borrowed
- An unavailable item may be reserved by an eligible member
- The system determines overdue status using the item's due date
