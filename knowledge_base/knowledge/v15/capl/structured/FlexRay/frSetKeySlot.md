# frSetKeySlot

> Category: `FlexRay` | Type: `function`

## Syntax

```c
void frSetKeySlot (long channel, long channelMask, long keySlotIndex, long keySlotId, long keySlotUsage);
```

## Description

Configures one of two possible key slots that are to be sent for a FlexRay bus.

The change will be applied with the next reset of the interface hardware (e.g. by resetFlexRayCC or resetFlexRayCCEx).

## Parameters

| Name | Description |
|---|---|
| channel | Channel number (or cluster number) |
| 1 | Channel A |
| 2 | Channel B |
| 3 | Channel A+B |
| keySlotIndex | Addresses the desired key slot (1 or 2). |
| keySlotId | This number designates a specific FlexRay slot in the static segment. Its value must be between 1 and 1023. |
| Value | Meaning |
| 0 | Off |
| 1 | Startup/Sync (Allowing Leading Coldstart) |
| 2 | Sync |
| 3 | Startup/Sync |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.2 | 7.2 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
