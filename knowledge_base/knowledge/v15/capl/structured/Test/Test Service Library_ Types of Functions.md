# Test Service Library: Types of Functions

> Category: `Test` | Type: `notes`

## Description

Check functions shall be identifiable easily. So the functions are to be prefixed in the following way:

Types of arguments (defined in CAPL) that can be handed over.

| Type | Explanation |
|---|---|
| Network | Network database symbol (or case sensitive string). |
| Node | Node database symbol (or case sensitive string). |
| Message | ID or database symbol of the message to check (or case sensitive string). |
| Signal | Database symbol of the signal to check, qualified with the message (or case sensitive signal short name). |
| Callback | Name of the function to call (signature is fixed). |
| Duration | Length of an interval with the unit of the current precision.(Default: milliseconds) |
| Check | Reference-ID of a check (type "dword"), returned on check creation. |

| Version 15© Vector Informatik GmbH |
|---|
