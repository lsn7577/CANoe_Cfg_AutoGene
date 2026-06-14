# J1939TestJoinDMWithoutSPNEvent

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestJoinDMWithoutSPNEvent( dword sourceAddr, dword pgn, dword spn )
long J1939TestJoinDMWithoutSPNEvent( dword sourceAddr, dbMsg message, dword spn )
```

## Description

Adds a new diagnostic message without SPN event to the 'joined events'. The function does not wait.

The parameter group must be able to contain a SPN, so only this parameter groups are allowed: DM1, DM2, DM6, DM12, DM23, DM27, DM28 and DM41-DM52.

## Parameters

| Name | Description |
|---|---|
| sourceAddr | source address of the PG or null address (0xFE) for wildcard |
| pgn | parameter group number, that is waited for |
| message | message from the database |
| spn | suspect parameter number on which disappearance it is waited for |

## Example

```c
long lret;
J1939TestJoinDMWithoutSPNEvent(10, 0xFF, 1119);
J1939TestJoinDMWithoutSPNEvent(20, 0xFF, 1119);

lret = J1939TestWaitForAnyJoinedEvent ( 500 );
switch(lret) {
  case 1: // first PG received
    break;
  case 2: // second PG received
    break;
  default: // error, timeout or constrain violation
    break;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 | 13.0 | — | — | 1.1 SP2 |
| Restricted To | — | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
