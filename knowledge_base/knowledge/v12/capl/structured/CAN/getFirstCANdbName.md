# getFirstCANdbName

> Category: `CAN` | Type: `function`

## Syntax

```c
dword getFirstCANdbName( char buffer[], dword size)
```

## Description

Finds out the name of the first assigned database.

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

| Since Version |
|---|
