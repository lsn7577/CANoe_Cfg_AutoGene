# J1939TestOnNMTChange

> Category: `J1939` | Type: `function`

## Syntax

```c
void J1939TestOnNMTChange( long ecuHandle, long reason );
```

## Description

The function can be implemented in your CAPL program. The J1939 Test Service Library calls this function, if the NMT table changes. The CAPL program can react on this changes.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | handle of the ECU, which has changedUse this handle with J1939TestNmtQueryAddress and J1939TestNmtQueryDeviceName. |
| reason | This parameter contains why this callback was called: 1: ECU did begin with Address Claiming (Address Claim PG was received) 2: ECU did successfully claim an address (250ms after Address Claim PG) 3: ECU lost its address, another ECU has a higher prior name |

## Return Values

—

## Example

```c
void J1939TestOnNMTChange( LONG ecuHandle, LONG reason ) {

  char dn[8];
  int address;

  J1939TestNmtQueryDeviceName( ecuHandle, dn );
  address = J1939TestNMTQueryAddress( ecuHandle );

  switch(reason) {
  case 1: // Begin claiming
    break;
  case 2: // Claiming completed successful (250ms after begin)
    break;
  case 3: // Lost address
    break;
  }
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
