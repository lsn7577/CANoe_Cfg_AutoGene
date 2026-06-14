# linTransmitHeader

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linTransmitHeader(dword frameId); // form 1
dword linTransmitHeader(linFrame frame); // form 2
```

## Description

Transmits a frame header for a specific LIN frame.

## Parameters

| Name | Description |
|---|---|
| frameId | ID of the LIN frame whose header will be transmitted. Value range: 0..63 |
| frame | The LIN frame whose header will be transmitted. |

## Return Values

Returns 1 if the transmission succeeded, otherwise 0.

## Example

```c
// Transmit a LIN header with the id 0x01

linFrame 0x01 frm1;
linTransmitHeader(frm1);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 | 10.0 | 13.0 | 13.0 | — | 2.2 |
| Restricted To | LIN | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
