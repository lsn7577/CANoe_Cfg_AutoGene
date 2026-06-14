# Chk_AddNode

> Category: `Test` | Type: `function`

## Syntax

```c
dword Chk_AddNode (dword aCheckId, Node aNode, dword aAddress, dword aac, dword ig, dword sys, dword sysi, dword fct, dword fcti, dword ecui, dword mc, dword in);
```

## Description

Adds a J1939 node to an existing check.

## Parameters

| Name | Description |
|---|---|
| aCheckId | Check Id of an existing check. |
| aNode | Name of the node to be checked. Must exist in database. |
| aAddress | Address of the node.0-253 or 0xFFFFFFFF if value of the node in database is used. |
| aac | Arbitrary Address Capable0..1 or 0xFFFFFFFF if value of the node in database is used. |
| ig | Industry Group0..7 or 0xFFFFFFFF if value of the node in database is used. |
| sys | Vehicle System Instance0..15 or 0xFFFFFFFF if value of database is used. |
| sysi | Vehicle System0..127 or 0xFFFFFFFF if value of the node in database is used |
| fct | Function0..255 or 0xFFFFFFFF if value of the node in database is used. |
| fcti | Function Instance0..31 or 0xFFFFFFFF if value of the node in database is used. |
| ecui | ECU Instance0..7 or 0xFFFFFFFF if value of the node in database is used. |
| mc | Manufacturer Code 0..2047 or 0xFFFFFFFF if value of the node in database is used. |
| in | Identity Number0.. 209715 or 0xFFFFFFFF if value of the node in database is used. |

## Example

```c
// checks the address claim violation of node N1
checkId = ChkCreate_J1939AddressClaimViolation ( N1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 200, 0x01);

// add node N2 to the check
Chk_AddNode (checkId, N2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1);
TestAddCondition(checkId);

// Start check
ChkControl_Start(checkId);

// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP3 | 13.0 | — | 14 | 1.1 SP2 |
| Restricted To | — | J1939 | J1939 | — | J1939 | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
