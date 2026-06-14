# diagGetDescriptionInformation

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetDescriptionInformation (char ecuQualifier[], char field[], char buffer[], dword bufferLen)
long diagGetDescriptionInformation (char field[], char buffer[], dword bufferLen)
```

## Description

Returns information on a diagnostic description, as stored in the database file itself.

## Parameters

| Name | Type | Description |
|---|---|---|
| ecuQualifier |  | Retrieves information for this diagnostic description. If not given, the currently selected target or description assigned to the ECU simulation is used. |
| Value of field | Meaning | Example |
| " " (empty string) | A short overview is returned | See below |
| DatabaseFormat | Database file type | "CDL", "ODX", ... |
| DatabaseVersion | Database file format version | "8.0.1100", "2.0.1" |
| Manufacturer | As stored in database | "Vector" |
| Version | Document version | "1.2" |
| LastHistoryChange | Last change history entry | "2015-02-25 Abc" |
| SaveNumber | As stored in database | "123" |
| TemplateLabel | As stored in database | "V7.1 A" |
| TemplateSaveNumber | As stored in database | "43" |
| buffer |  | The value is written into this array. |
| bufferLen |  | Capacity of the array |

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
