# KLine_CreateECURepresentation

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_CreateECURepresentation(dword channel)
```

## Description

Initialize K-Line ECU communication on given channel.

## Parameters

| Name | Description |
|---|---|
| channel | Number of the hardware channel. |

## Return Values

On success 0, otherwise a value less than 0.

## Example

```c
on preStart
{
   long klineHandle;
   long channelNo;

   channelNo = DiagGetCommParameter( "CANoe.ChannelNumber");
   klineHandle = KLine_CreateECURepresentation( channelNo);
   write( "KLine_CreateECURepresentation at K-Line%d returns %d", channelNo, klineHandle);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 SP4 | — | — | — | 1.1 SP2 |
| Restricted To | — | K-Line Real bus mode Online mode ECU simulation | — | — | — | K-Line Real bus mode Online mode ECU simulation |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
