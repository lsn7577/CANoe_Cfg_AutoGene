# linGetChecksum

> Category: `LIN` | Type: `function`

## Syntax

```c
byte linGetChecksum(linFrame linFrame); form 1
byte linGetChecksum(linCSError linCsError); // form 2
```

## Description

Returns the checksum of a LIN frame or LIN checksum error.

Checksum model (classic/enhanced) is determined automatically.

## Parameters

| Name | Description |
|---|---|
| linFrame | LIN frame object |
| linCsError | LIN checksum error object |

## Return Values

Calculated checksum

## Example

Get the checksum of a received LIN frame with name myframe

```c
on linFrame myframe
{
byte checksum;
checksum = linGetChecksum(this);
}
or
// Calculate the checksum of a LIN frame object 
...
byte checksum;
// create a LIN frame object
linFrame 0x1 myLinFrame = { dlc = 1, byte(0) = 1 };
// calculate its checksum
checksum = linGetChecksum(myLinFrame);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.0 | 6.0 | 13.0 | 13.0 | — | 1.0 |
| Restricted To | LIN | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
