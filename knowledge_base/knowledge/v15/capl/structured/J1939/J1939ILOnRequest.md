# J1939ILOnRequest

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILOnRequest( long rqPGN, long sourceAddr )
long J1939ILOnRequest( long rqPGN, long sourceAddr, long destinationAddress )
```

## Description

This callback function is called from the J1939 IL if a request (0xEA00) is received.

## Parameters

| Name | Description |
|---|---|
| rqPGN | requested PGN |
| sourceAddr | source address from which the request was sent |
| destinationAddress | destination address on which the request was sent |

## Example

```c
LONG J1939ILOnRequest( LONG rqPGN, LONG sourceAddr )
{
  switch( rqPGN ) {
  case 0xFF02:
    return 2; // send NACK
  }
  return 1;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | 13.0 | — | — | — |
| Restricted To | — | J1939 | J1939 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
