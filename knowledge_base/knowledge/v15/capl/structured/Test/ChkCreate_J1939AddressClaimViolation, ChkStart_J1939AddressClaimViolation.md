# ChkCreate_J1939AddressClaimViolation, ChkStart_J1939AddressClaimViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_J1939AddressClaimViolation (Node aNode, dword aAddress, dword aac, dword ig, dword sys, dword sysi, dword fct, dword fcti, dword ecui, dword mc, dword in, dword aTimeout, dword aFlags, char[] callback1);
dword ChkStart_J1939AddressClaimViolation (Node aNode, dword aAddress, dword aac, dword ig, dword sys, dword sysi, dword fct, dword fcti, dword ecui, dword mc, dword in, dword aTimeout, dword aFlags, char[] callback1);
```

## Description

Observes the Address Claiming of a J1939 node. The specified node must respond to a Request for Address Claim.

Optionally the check allows sending other messages, only if an Address Claim message (0xEE00) of the node is received first.

You can add further nodes to this check with Chk_AddNode.

## Parameters

| Name | Description |
|---|---|
| aNode | Name of the node to be checked. Must exist in database. |
| aAddress | Address of the node.0-253 or -1 (or 0xFFFFFFFF) if value of the node in database is used. |
| aac | Arbitrary Address Capable0..1 or -1 (or 0xFFFFFFFF) if value of the node in database is used. |
| ig | Industry Group0..7 or -1 (or 0xFFFFFFFF) if value of the node in database is used. |
| sys | Vehicle System0..127 or -1 (or 0xFFFFFFFF) if value of database is used. |
| sysi | Vehicle System Instance0..15 or -1 (0xFFFFFFFF) if value of the node in database is used. |
| fct | Function0..255 or -1 (or 0xFFFFFFFF) if value of the node in database is used. |
| fcti | Function Instance0..31 or -1 (or 0xFFFFFFFF) if value of the node in database is used. |
| ecui | ECU Instance0..7 or -1 (or 0xFFFFFFFF) if value of the node in database is used. |
| mc | Manufacturer Code 0..2047 or -1 (or 0xFFFFFFFF) if value of the node in database is used. |
| in | Identity Number0.. 2097151 or -1 (or 0xFFFFFFFF) if value of the node in database is used. |
| aTimeout | Within this time a Request for Address Claim has to be responded.Default unit [ms], if not changed with ChkConfig_SetPrecision. |
| aFlags | Bit 0: Allow address usage before Address Claim. Bit 1: Allow Address Claim messages from non-configured nodes. Bit 2: Allow claiming of other address than configured. |
| callback1 | This parameter is optional. Name of the callback which is called when the check fails.Signature: void Callback( dword checkId ) |
| callback2 | This parameter is optional. Name of the callback which is called when the check fails.Signature: void Callback( TestCheck check ) |

## Example

```c
TestCheck c;
// checks the address claim violation of node N1
c = TestCheck::CreateJ1939AddressClaimViolation( N1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 200, 0x01);

// add node N2 to the check
c.AddNode (N2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1);
TestAddCondition(c);

// Start check
c.start();

// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(c);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP3 | 13.0 | — | — | 1.1 SP2 |
| Restricted To | — | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
