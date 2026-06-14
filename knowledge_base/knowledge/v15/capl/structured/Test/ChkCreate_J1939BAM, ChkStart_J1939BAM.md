# ChkCreate_J1939BAM, ChkStart_J1939BAM

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_J1939BAM(dword min, dword max, char[] callback1);
dword ChkCreate_J1939BAM(dword originatorAddress, dword min, dword max, char[] callback1);
dword ChkCreate_J1939BAM(Node origninatorNode, dword min, dword max, char[] callback1);
dword ChkStart_J1939BAM(dword min, dword max, char[] callback1);
dword ChkStart_J1939BAM(dword orginatorAddress, dword min, dword max, char[] callback1);
dword ChkStart_J1939BAM(Node origninatorNode, dword min, dword max, char[] callback1);
```

## Description

Observes the BAM transport protocol. It is possible to observe all BAM transmissions or only the transmission of a specific originator node.

## Parameters

| Name | Description |
|---|---|
| originatorNode | Originator node from database |
| originatorAddress | Originator address Possible values:0 – 253: Observe originator node with this address254, -1 (or 0xFFFFFFFF): Observe all nodes |
| min | Minimum distance [ms] (Default 50ms) |
| max | Maximum distance [ms] (Default 200ms) |
| callback1 | This parameter is optional. Name of the callback which is called when the check fails.Signature: void Callback( dword checkId ) |
| callback2 | This parameter is optional. Name of the callback which is called when the check fails.Signature: void Callback( TestCheck check ) |

## Example

```c
// checks the BAM transport protocol of node N1
checkId = ChkStart_J1939BAM(N1, 100, 200);
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
