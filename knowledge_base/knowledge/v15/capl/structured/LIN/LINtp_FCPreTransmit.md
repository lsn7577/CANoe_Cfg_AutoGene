# LINtp_FCPreTransmit

> Category: `LIN` | Type: `function`

## Syntax

```c
void LINtp_FCPreTransmit(byte fcData);
```

## Description

When the usage of FlowControl frames has been activated with LINtp_ActivateFCTransmission, each FlowControl frame is forwarded to this callback function before it is sent.

## Parameters

| Name | Description |
|---|---|
| fcData | Data of the FC frame. |

## Return Values

—

## Example

```c
void LINtp_FCPreTransmit( BYTE fcData[])
{
  write( "FlowControl to be sent: %02x %02x %02x %02x (%d byte)"
  , fcData[0] , fcData[1] , fcData[2] , fcData[3], elcount(fcdata));
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5 | — | — | — | — |
| Restricted To | — | LIN Real bus mode | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
