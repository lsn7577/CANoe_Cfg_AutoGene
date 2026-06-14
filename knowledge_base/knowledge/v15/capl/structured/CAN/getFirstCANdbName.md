# getFirstCANdbName

> Category: `CAN` | Type: `function`

## Syntax

```c
dword getFirstCANdbName( char buffer[], dword size)
```

## Description

Finds out the name of the first assigned database.

## Parameters

| Name | Description |
|---|---|
| buffer | Buffer in which the database name is written. |
| size | Size of the buffer in Byte. |

## Return Values

If successful unequal 0, otherwise 0.

## Example

```c
on start
{
char buffer[256];
dword pos;

pos = GetFirstCANdbName( buffer, elcount( buffer));
//Finds the name of the first database.
//If a database is found, "pos" contains the value 1
//If none is found "pos" contains 0

while ( 0 != pos)
{
write( "CANdb: %s", buffer);
pos = GetNextCANdbName( pos, buffer, elcount( buffer));
//Finds the names of other databases.
//If any other databases are found
//"pos" contains the value 2, 3, etc
//If no further databases are found
//"pos" contains 0 and the loop is exited
}
}

Example to find the third database

on key '3'
{
char buffer[256];
dword pos;
dword DbcNumber = 2; //Position number of the second database
pos = GetNextCANdbName(DbcNumber, buffer, elcount(buffer));
//Returns the name of the third database.
//Return value "pos" contains the value 3.
//If no third database is found "pos" contains 0.

write( "Database position number : %d Database name : %s",pos, buffer);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 4.0 | 4.0 | 13.0 | — | — | 1.0 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | — | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
