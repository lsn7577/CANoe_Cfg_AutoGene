# ARILCalculateCRC

> Category: `AUTOSARpduIL` | Type: `function`

## Syntax

```c
long ARILCalculateCRC (char aMsgName[], cahr sigGroupName[], BYTE payload[], dword aPayloadLength, dword crc[]);
```

## Description

Calculates the CRC of the PDU according to the given payload.

## Parameters

| Name | Description |
|---|---|
| aMsgName | The symbolic name of a PDU in the database. |
| sigGroupName | Full name of the designated signal group. |
| payload | Byte array with the full payload of the PDU. |
| aPayloadLength | The length of the payload buffer. |
| crc | Returns the calculated CRC value. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP2 | 14 | 14 | — | — |
| Restricted To | — | CAN Ethernet FlexRay | CAN Ethernet FlexRay | CAN Ethernet FlexRay | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
