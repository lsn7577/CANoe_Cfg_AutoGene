# mostGetAllocTable

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostGetAllocTable(long channel, byte buffer[], long buffersize);
```

## Description

The mostGetAllocTable() function copies the MOST Allocation Table (max. 60 bytes) to a local CAPL buffer. It must be verified that the buffer has the required size (buffersize).

The Allocation Table contains the reservation status of the synchronous MOST channels.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected Interface. |
| buffer | Destination buffer |
| buffersize | Destination buffer size |

## Return Values

See error codes

## Example

```c
byte allocTable[60];
// copy allocation table to local buffer
mostGetAllocTable(mostGetChannel(), allocTable, elcount(allocTable));
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.1 | 5.1 | — | — | — | —✔ |
| Restricted To | MOST25 After measurement start Not in Stopmeasurement | MOST25 After measurement start Not in Stopmeasurement | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
