# J1939TestWaitForDMWithSPN

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestWaitForDMWithSPN( dword sourceAddr, dword pgn, dword spn, dword timeout )
long J1939TestWaitForDMWithSPN( dword sourceAddr, pg pgBuffer, dword pgBufferSize, dword spn, dword timeout )
long J1939TestWaitForDMWithSPN( dword sourceAddr, dbMsg message, dword spn, dword timeout )
long J1939TestWaitForDMWithSPN( dbNode source, dbMsg message, dword spn, dword timeout )
```

## Description

The function waits until a defined parameter group and a defined Suspect Parameter Number (SPN) is received or a timeout occurred.

The parameter group must be able to contain a SPN, so only this parameter groups are allowed: DM1, DM2, DM6, DM12, DM23, DM27, DM28 and DM41-DM52.

## Parameters

| Name | Description |
|---|---|
| sourceAddr | source address of the PG or null address (0xFE) to ignore the source address |
| source | node from database, see node definition |
| pgn | parameter group number that is waited for |
| pgBuffer | parameter group, that is filled with the received data |
| pgBufferSize | size of parameter group |
| message | message from the database |
| spn | suspect parameter number that is waited for |
| timeout | timeout in [ms] or 0 to deactivate the timeout |

## Example

```c
long lret;
lret = J1939TestWaitForDMWithSPN(10, 0xF123, 110, 500 );

switch(lret) {
  case 1:
    break;
  default: // error, timeout or constraint violation
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
