# Iso11783UpdateTable

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783UpdateTable( char busName[] );
```

## Description

Updates the network table.

The function deletes the content of the current table and initiates the RequestPGN that was used to request Address Claiming. After that, the table is restructured. With busName, you assign a table which is used in a network. A node which was displaced from the network if it has lost the Address Claiming, will be placed in the network table with the NULL address. After calling this function, all contents of the table will deleted and the table will update itself by sending a request. All ECU which sends the NULL address will be ignored. Only the active nodes will be inserted into the table.

## Parameters

| Name | Description |
|---|---|
| busName | Bus name or "default" |

## Return Values

0 on success or error code

## Example

```c
Iso11783UpdateTable( "default" 
 );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | Iso11783 | Iso11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
