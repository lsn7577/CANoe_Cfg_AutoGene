# FSIL_OnRxMessage

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_OnRxMessage( pg * rxPG );
```

## Description

Is called from the FS IL if the FS IL receives the parameter group, namely before the parameter group is processed by the FS IL. The message data can be manipulated in the callback method or handling of the message by the IL can be suppressed.

Usage

## Parameters

| Name | Description |
|---|---|
| rxPG | Message which is received |

## Example

The following example blocks the RQST of the pgn = 0x5** (case 5) and replace the RQST of the pgn = 0x3** by the RQST of the pgn = 0x4** (case 3).

```c
long FSIL_OnRxMessage( pg * rxPG )
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
| Since Version | — | 12.0 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
