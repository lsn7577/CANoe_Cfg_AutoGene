# VTIL_BlockRxMessage

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_BlockRxMessage(dword pgn, dword sourceAddress, qword filterMask, qword filterValue); // form 1
long VTIL_BlockRxMessage(dbNode node, dword pgn, dword sourceAddress, qword filterMask, qword filterValue); // form 2
```

## Description

Prevents processing of a received message by the interaction layer.

The message to block is specified by PGN, destination source address and a part of the first eight data bytes.

To revert this command you can use VTIL_ResetBlockedRxMessage or VTIL_ResetAllBlockedRxMessages.

## Parameters

| Name | Description |
|---|---|
| pgn | The message with this PGN shall be blocked. |
| sourceAddress | 0 - 255: The message which is sent to this address shall be blocked. 0xFFFFFFFF (-1): The source address of the message doesn’t matter. |
| filterMask | Defines the bits of the message which shall be used to identify the message. |
| filterValue | Defines the value of the bits of the message which shall be used to identify the message. If the value of the masked bits of a received message is equal to this value then the data of the message is blocked. |
| node | Simulation node to apply the function. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | 13.0 | — | — | 3.0 SP3 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
