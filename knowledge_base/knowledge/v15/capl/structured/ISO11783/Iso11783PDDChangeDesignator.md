# Iso11783PDDChangeDesignator

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783PDDChangeDesignator( dword ecuHandle, word objectID, char asciiDesignator[] );
long Iso11783PDDChangeDesignator( dword ecuHandle, word objectID, char asciiDesignator[], byte encoding );
```

## Description

The function sends a Change Designator message with a new object designator to the Task Controller.

The first variant converts the ASCII designator string to an UTF-8 string if the supported version is 2 or higher.

In the second variant you can specify if the designator string shall encoded to UTF-8 or not.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU. The handle must be created with Iso11783CreateECU beforehand or ZERO for general parameters. |
| objectID | ID of the object |
| asciiDesignator | New object designator |
| encoding | Specifies if the designator is encoded before it is transmitted or not 0: designator string is not encoded 1: designator string is encoded to UTF-8 |

## Return Values

error code

## Example

Example 1

Example 2 (avoid encoding because string is already UTF-8 string encoded)

```c
if (Iso11783PDDChangeDesignator( ecuHandle, 1, "myNewDesignator" ) == 0) {
  write( "Change Designator command is sent successfully" );
}
char euroSign[255];
euroSign.byte(0) = 0xE2;
euroSign.byte(1) = 0x82;
euroSign.byte(2) = 0xAC;
euroSign.byte(3) = 0;

if (Iso11783PDDChangeDesignator( ecuHandle, 1, euroSign, 0 ) == 0) {
  write( "Command so change designator to '€' is sent successfully" );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
