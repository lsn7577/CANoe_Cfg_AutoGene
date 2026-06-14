# J1939AppRxIndication

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939AppRxIndication( long ecuHandle, long srcAddr, long dstAddr, long length, long pgnum );
```

## Description

The callback function indicates to the user that a parameter group has been received. It is not possible in CAPL to receive PG data through a callback function. For this reason, the data must be explicitly requested within the callback function with J1939GetRxData().

It should be noted that this function is only called once for each logical ECU within a node when global PGs are received.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | ECU handle |
| srcAddr | source address |
| dstAddr | destination address |
| length | number of received data |
| pgnum | PGN of the received parameter group |

## Return Values

—

## Example

```c
dword J1939AppRxIndication( LONG ecuHdl, LONG srcAddr, LONG dstAddr, LONG len, LONG pgNumber)
{
  char data[50];
  J1939GetRxData( elCount(data), data );
  /* user code */
  return 0;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | J1939 | J1939 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
