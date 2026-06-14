# J1939ILOnRxMessage

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILOnRxMessage( pg * rxPG )
```

## Description

This callback function is called from the J1939 IL if the J1939 IL receives the parameter group, namely before the parameter group is processed by the J1939 IL. The message data can be manipulated in the callback method or handling of the message by the IL can be suppressed.

Usage

## Parameters

| Name | Description |
|---|---|
| rxPG | message which is received |

## Example

```c
long J1939ILOnRxMessage( pg * rxPG )
{
  if(rxPG.PGN == 0xEA00)
  {
    switch(rxPG.BYTE(1))
    {
    case 3:
      rxPG.BYTE(1) = 4;
      return 1;

    case 5:
      return 0;

    default:
      return 1;
    }
  }
  return 1;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 | 13.0 | — | — | — |
| Restricted To | — | J1939 | J1939 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
