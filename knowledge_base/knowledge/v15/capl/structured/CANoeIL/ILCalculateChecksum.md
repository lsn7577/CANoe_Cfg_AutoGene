# ILCalculateChecksum

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILCalculateChecksum (char pduNamme[], long type, BYTE payload[], long payloadLength, BYTE crc [])
```

## Description

Calculates the corresponding CRC checksum based on the payload. The correct offset is calculated from the database using the PDU name.

## Parameters

| Name | Description |
|---|---|
| pduName | Name of the PDU. |
| type | type = 0 : CRCtype = 1 : CHK |
| payload | Payload for which the checksum is to be calculated. |
| payloadLength | Number of data bytes in payload. |
| crc | The calculated checksum. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 SP5 | 14 | 14 | — | — |
| Restricted To | — | FlexRay Simulation nodes | FlexRay Simulation nodes | FlexRay Simulation nodes | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
