# mostSetSyncSpdifMode

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetSyncSpdifMode(long channel, long mode);
```

## Description

Sets the timing mode for the S/PDIF signal.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface |
| 0 | S/PDIF slave. |
| 1 | S/PDIF master. |

## Return Values

See error codes

## Example

Use Cases:

External S/PDIF sink device connected to the S/PDIF Out connector of the VN2610

In this case the VN2610 is S/PDIF Master and the S/PDIF mode has to be set accordingly (mode = 1).

External S/PDIF source device connected to the S/PDIF In connector of the VN2610

In this case the VN2610 is S/PDIF Slave and the S/PDIF mode has to be set accordingly (mode = 0).

More S/PDIF examples see CANoe online help MOST Access to Digital Audio Channels (S/PDIF In and Out).

```c
on key 's'
{
  long channel = 1;
  mostSetSyncSpdifMode( channel, 1 );
}

on key 's'
{
  long channel = 1;
  mostSetSyncSpdifMode( channel, 0 );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.0 | 6.0 | — | — | — | —✔ |
| Restricted To | MOST25 MOST150 | MOST25 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
