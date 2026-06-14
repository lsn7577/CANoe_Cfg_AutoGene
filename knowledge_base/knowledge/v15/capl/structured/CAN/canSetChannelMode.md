# canSetChannelMode

> Category: `CAN` | Type: `function`

## Syntax

```c
long canSetChannelMode(long channel, long gtx, long gtxreq);
```

## Description

Activates/deactivates the TXRQ and Tx of the CAN controller. This function does nothing with the Ack bit.

## Parameters

| Name | Description |
|---|---|
| channel | CAN channel |
| 0 | tx off |
| 1 | tx on |
| 0 | gtxreq off |
| 1 | gtxreq on |

## Example

```c
on key 't'
{
   long channel =2;
   char gtx =1;
   char gtxreq =1;
   canSetChannelMode(channel,gtx,gtxreq);
   Write("Mode set to tx=%d, txreq=%d",gtx,gtxreq);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.0 | 5.0 | 13.0 | — | — | 1.0 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
