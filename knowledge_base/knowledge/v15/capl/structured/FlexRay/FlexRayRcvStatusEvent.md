# FlexRayRcvStatusEvent

> Category: `FlexRay` | Type: `function`

## Syntax

```c
FlexRayRcvStatusEvent (long msgTime, int channel, long statusType, long infomask1, long infomask2, long infomask3);
```

## Description

This function is a callback and is called by the tool!

The callback occurs when the FlexRay Communication Controller (CC) has synchronized with the bus or the synchronization fails.

## Parameters

| Name | Type | Description |
|---|---|---|
| msgTime |  | Event time stamp. |
| channel |  | Channel in the tool that selects the CC. Should be set to 1 by default (since the tool currently only supports one FlexRay CC). |
| Type |  | Meaning |
| 0x0001 |  | "Bus Synchronization" status is included. |
| 0x0002 |  | Received symbol |
| Type | Bit Value | Meaning |
| 0x0001 | 0 | CC unable to synchronize with the bus. |
| 1 |  | CC is synchronized to the bus. |
| 1 |  | CAS |
| 2 |  | MTS |
| 3 |  | Wakeup |
| 4 |  | Not specified |
| Example 0x00260004: not specified signal with the length 38. |  |  |
| infomask2 |  | If statusType == 1: Not used. If statusType == 2: Symbol receiving cycle. |
| infomask3 |  | If statusType == 1: Not used. If statusType == 2: Channel mask (A=1 / B=2 / AB = 3): Channel the symbol was received. |

## Return Values

—

## Example

```c
variables
{
   int busIsSynchronized = 0;
}
FlexRayRcvStatusEvent (long msgTime, int channel, long statusType, long infomask1, long infomask2, long infomask3)
{
   if (statusType & 0x00000001)
   {
      if (infomask1 & 0x00000001)
      {
         busIsSynchronized = 1;
         Write("FR StatusEvent: Bus (channel %d) is synchronized.", channel);
      }
      else
      {
         Write("FR StatusEvent: Bus (channel %d) lost synchronization.", channel);
         if (busIsSynchronized == 1) ResetFlexRayCC(channel);
         busIsSynchronized = 0;
      }
    }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.2 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
