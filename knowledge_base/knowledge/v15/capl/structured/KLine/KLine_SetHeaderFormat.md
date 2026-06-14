# KLine_SetHeaderFormat

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_SetHeaderFormat(long useAddresses, long forceLengthByte)
```

## Description

Configures the used header format.

## Parameters

| Name | Description |
|---|---|
| useAddresses | 0: Address bytes are not used.1: Address bytes are used. |
| forceLengthByte | 0: No Length byte will be sent.1: Length byte will always be sent.2: Length byte will be sent for frames greater than 63 bytes. |

## Return Values

On success 0, otherwise a value less than 0.

## Example

```c
KLine_SetHeaderFormat(0, 0); // A one byte header will be sent.
KLine_SetHeaderFormat(0, 1); // A two byte header will be sent.
KLine_SetHeaderFormat(1, 0); // A three byte header will be sent.
KLine_SetHeaderFormat(1, 1); // A four byte header will be sent.
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 | 8.0 | — | — | — | 1.1 SP2 |
| Restricted To | K-Line Real bus mode ECU tester | K-Line Real bus mode ECU simulation ECU tester | — | — | — | K-Line Real bus mode ECU simulation ECU tester |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
