# ChkCreate_J1939RTSCTS, ChkStart_J1939RTSCTS

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_J1939RTSCTS(dword t1, dword t2, dword t3, dword t4, char[] callback1);
dword ChkCreate_J1939RTSCTS(dword senderAddress, dword responderAddress, dword t1, dword t2, dword t3, dword t4, char[] callback1);
dword ChkCreate_J1939RTSCTS(Node origninatorNode, Node responderNode, dword t1, dword t2, dword t3, dword t4, char[] callback1);
dword ChkStart_J1939RTSCTS(dword t1, dword t2, dword t3, dword t4, char[] callback1);
dword ChkStart_J1939RTSCTS(dword orginatorAddress, dword responderAddress, dword t1, dword t2, dword t3, dword t4, char[] callback1);
dword ChkStart_J1939RTSCTS(Node origninatorNode, Node responderNode, dword t1, dword t2, dword t3, dword t4, char[] callback1);
```

## Description

Observes the RTS/CTS transport protocol. It is possible to observe all RTS/CTS transmissions or only the transmission of a specific send node.

## Parameters

| Name | Description |
|---|---|
| originatorNode | Originator node from database. |
| responderNode | Responder node from database. |
| originatorAddress | Originator address Possible values: 0 – 253: Observe originator node with this address254, -1 (or 0xFFFFFFFF): Observe all originator nodes |
| responderAddress | Responder address Possible values: 0 – 253, 255: Observe responder node with this address 254, -1 (or 0xFFFFFFFF): Observe all responder nodes |
| t1 | Timeout T1 [ms] (Default 750ms) |
| t2 | Timeout T2 [ms] (Default 1250ms) |
| t3 | Timeout T3 [ms] (Default 1250ms) |
| t4 | Timeout T4 [ms] (Default 1050ms) |
| callback1 | This parameter is optional. Name of the callback which is called when the check fails. Signature: void Callback( dword checkId ) |
| callback2 | This parameter is optional. Name of the callback which is called when the check fails. Signature: void Callback( TestCheck check ) |

## Example

```c
// checks the RTS/CTS transport protocol between node N1 and node N2
checkId = ChkStart_J1939RTSCTS(N1, N2, 750, 1250, 1250, 1050);
TestAddCondition(checkId);

// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5 | 13.0 | — | — | 2.0 |
| Restricted To | — | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
