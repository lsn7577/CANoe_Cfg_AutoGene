# diagGetDescriptionInformation

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetDescriptionInformation (char ecuQualifier[], char field[], char buffer[], dword bufferLen)
```

## Description

Returns information on a diagnostic description, as stored in the database file itself.

## Return Values

Number of characters written into the array, or error code. If a value is not defined in the database, 0 and an empty string are returned.

## Example

```c
char buffer[300];
DiagGetDescriptionInformation( "ECU1", "", buffer, elcount(buffer));
write( buffer);
/* Example output:
Qualifier: ECU1
Name: ABCD2015
File: C:\Projects\2015\R123\ABCD.cdd
Manufacturer: Vector
Last history change: 2014-07-11 08:32:23+02:00
File version: 1.3 #132
Template version: 14.20.19 #1
*/
DiagSetTarget( "ECU1");
DiagGetDescriptionVersion( buffer, elcount(buffer));
// returns "1.3"
```

## Availability

| Since Version |
|---|
