# VTIL_ResetManipulatedMessage

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_ResetManipulatedMessage( dword pgn, dword destinationAddress, qword filterMask, qword filterValue ); // form 1
long VTIL_ResetManipulatedMessage( dbNode node, dword pgn, dword destinationAddress, qword filterMask, qword filterValue ); // form 2
```

## Description

Resets the change of a single ISO11783VTIL_ManipulateMessage call. The corresponding message is specified by PGN, destination address and a part of the first eight data bytes.

## Parameters

| Name | Description |
|---|---|
| pgn | Use same value as in ISO11783VTIL_ManipulateMessage to stop manipulation of the message. |
| destinationAddress | Use same value as in ISO11783VTIL_ManipulateMessage to stop manipulation of the message. |
| filterMask | Use same value as in ISO11783VTIL_ManipulateMessage to stop manipulation of the message. |
| filterValue | Use same value as in ISO11783VTIL_ManipulateMessage to stop manipulation of the message. |
| node | Simulation node to apply the function. |

## Example

See example of ISO11783VTIL_ManipulateMessage.

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
