# getSignalName

> Category: `CAN` | Type: `function`

## Syntax

```c
char[] getSignalName(caplCanMessage* msg, dword startBit); // form 1
char[] getSignalName(caplAutosarPDU* pdu, dword startBit); // form 2
```

## Description

Finds out the signal name at a specified start index inside a CAN message (form 1).

Finds out the signal name at a specified start index inside a PDU (form 2).

## Parameters

| Name | Description |
|---|---|
| msg | CAN message. |
| pdu | AUTOSAR PDU. |
| startBit | First bit of the signal of the AUTOSAR PDU or CAN message. |

## Return Values

Returns the signal name at a given start index inside a CAN message. Start index is defined in DBC Editor (form 1).
Returns signal name at a given start index inside a PDU. Start index is defined with AUTOSAR Explorer (form 2).

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 14 | 14 | 14 | — | — | 5.0 SP3 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | — | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
