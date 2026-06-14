# diagGetDescriptionVersion

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetDescriptionVersion (char buffer[], dword bufferLen)
long diagGetDescriptionVersion (char ecuQualifier[], char buffer[], dword bufferLen)
```

## Description

Returns information on a diagnostic description, as stored in the database file itself.

## Parameters

| Name | Description |
|---|---|
| ecuQualifier | Retrieves information for this diagnostic description. If not given, the currently selected target or description assigned to the ECU simulation is used. |
| buffer | The value is written into this array. |
| bufferLen | Capacity of the array |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5 SP2 | — | — | — | 2.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
