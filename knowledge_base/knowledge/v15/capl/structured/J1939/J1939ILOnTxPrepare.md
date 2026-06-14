# J1939ILOnTxPrepare

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILOnTxPrepare( pg * txPG )
```

## Description

This callback function is called from the J1939 IL before a parameter group is sent. The signal value can be updated in the callback or sending of the message can be suppressed.

## Parameters

| Name | Description |
|---|---|
| txPG | message which should be sent |

## Example

```c
long J1939ILOnTxPrepare( pg * txPG )
{
  switch( txPG.PGN ) {
  case 0xFF01:
    txPG.BYTE(0) = 10; // update first byte
    break;
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
