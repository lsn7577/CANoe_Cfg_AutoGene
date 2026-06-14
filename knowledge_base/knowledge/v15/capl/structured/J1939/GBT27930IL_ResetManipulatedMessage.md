# GBT27930IL_ResetManipulatedMessage

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_ResetManipulatedMessage( dword pgn, dword destinationAddress, qword filterMask, qword filterValue ); // form 1
long GBT27930IL_ResetManipulatedMessage( dbNode node, dword pgn, dword destinationAddress, qword filterMask, qword filterValue ); // form 2
```

## Description

Resets the change of a single GBT27930IL_ManipulateMessage call. The corresponding message is specified by PGN, destination address and a part of the first eight data bytes.

## Parameters

| Name | Description |
|---|---|
| pgn | Use same value as in GBT27930IL_ManipulateMessage to stop manipulation of the message. |
| destinationAddress | Use same value as in GBT27930IL_ManipulateMessage to stop manipulation of the message. |
| filterMask | Use same value as in GBT27930IL_ManipulateMessage to stop manipulation of the message. |
| filterValue | Use same value as in GBT27930IL_ManipulateMessage to stop manipulation of the message. |
| node | Simulation node to apply the function. |

## Example

See example of GBT27930IL_ManipulateMessage.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | — | J1939 and Smart Charging | J1939 and Smart Charging | — | — | form 2 J1939 and Smart Charging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
