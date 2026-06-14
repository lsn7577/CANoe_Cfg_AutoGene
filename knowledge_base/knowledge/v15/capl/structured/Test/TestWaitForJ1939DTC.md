# TestWaitForJ1939DTC

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForJ1939DTC (dword sourceAddress, Message message, dword spn, dword timeout); // form 1
long TestWaitForJ1939DTC (dword sourceAddress, dword pgn, dword spn, dword timeout); // form 2
long TestWaitForJ1939DTC (Node node, Message message, dword spn, dword timeout); // form 3
long TestWaitForJ1939DTC (Node node, dword pgn, dword spn, dword timeout); // form 4
long TestWaitForJ1939DTC (dword sourceAddress, Message message, dword spn, word fmi, word oc, dword timeout); // form 5
long TestWaitForJ1939DTC (dword sourceAddress, dword pgn, dword spn, word fmi, word oc, dword timeout); // form 6
long TestWaitForJ1939DTC (Node node, Message message, dword spn, word fmi, word oc, dword timeout); // form 7
long TestWaitForJ1939DTC (Node node, dword pgn, dword spn, word fmi, word oc, dword timeout); // form 8
```

## Description

Waits until a defined Parameter Group and a defined Diagnostic Trouble Code (DTC) is received or a timeout occurred.

The affected message (specified by the Parameter Group number pgn or the database object message) must be able to contain a DTC, so only this parameter groups are allowed: DM1, DM2, DM4, DM6, DM12, DM23, DM24, DM27, DM28, DM31, DM35 and DM41-DM54.

## Parameters

| Name | Description |
|---|---|
| message | Message containing the specified DTC. Must be a J1939 Parameter Group. |
| pgn | Parameter Group Number (with data page) of the message containing the specified DTC. |
| node | Sender of the message containing the specified DTC. |
| sourceAddress | Source address of the message containing the specified DTC 0xFFFFFFFF if source address is to be ignored. |
| spn | Suspect Parameter Number of the specified DTC 0xFFFFFFFF if spn is to be ignored. |
| fmi | Failure Mode Identifier of the specified DTC 0xFFFF if fmi is to be ignored. |
| oc | Occurrence Counter of the specified DTC 0xFFFF if oc is to be ignored. |
| timeout | Maximum time to wait [ms]. 0 if timeout is to be ignored. |

## Example

```c
long result;

// waits for the occurrence of DTC with SPN=96 and FMI=12 within message DM1 (pgn=0xFECA) from node with address=0x2
result = TestWaitForJ1939DTC(0x2, 0xFECA, 96, 12, 0xFFFF, 2000);

// waits for the occurrence of DTC with SPN=98765 and OC=1 within message DM2 (pgn=0xFECB) from node with address=0x3
result = TestWaitForJ1939DTC(0x3, 0xFECB, 98765, 0xFFFF, 1, 2000);

// waits for the occurrence of DTC with OC=10 within message DM35 (pgn=0x9F00) from any node
result = TestWaitForJ1939DTC(0xFFFFFFFF, 0x9F00, 0xFFFFFFFF, 0xFFFF, 10, 2000);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5: form 1, 2, 3, 4 12.0: form 5, 6, 7, 8 | 13.0 | — | — | 2.0: form 1, 2, 3, 4 4.0: form 5, 6, 7, 8 |
| Restricted To | — | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
