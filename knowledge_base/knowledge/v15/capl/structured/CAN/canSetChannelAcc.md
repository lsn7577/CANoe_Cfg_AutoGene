# canSetChannelAcc

> Category: `CAN` | Type: `function`

## Syntax

```c
long canSetChannelAcc(long channel, dword code, dword mask);
```

## Description

Via an acceptance filter the CAN controllers control which received messages are sent through to CANoe.Some controller chips, such as the SJA 1000, expect partitioning into acceptance mask and acceptance code.

## Parameters

| Name | Description |
|---|---|
| channel | CAN channel |
| code | Acceptance code |
| mask | Acceptance mask |

## Example

```c
on key 'a'
{
/*
To distinguish whether the filter is for standard or extended identifier. For extended identifiers the MSB of the code and mask are set.
Description:
Different ports may have different filters for a channel. If the CAN hardware cannot implement the filter, the driver virtualises filtering.
Accept if ((id ^ code) & mask) == 0). 
*/
   long channel =2;
   dword code=0x10;
   dword mask=0x10;
   canSetChannelAcc(channel,code,mask);
   write("channel mask set");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.0 | 5.0 | 13.0 | — | — | 1.0 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
