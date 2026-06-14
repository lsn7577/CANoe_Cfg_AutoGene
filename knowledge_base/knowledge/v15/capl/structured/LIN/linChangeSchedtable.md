# linChangeSchedtable

> Category: `LIN` | Type: `function`

## Syntax

```c
long linChangeSchedTable(dword tableIndex);
long linChangeSchedTable(dword tableIndex, dword slotIndex);
long linChangeSchedTable(dword tableIndex, dword slotIndex, dword onSlotIndex);
```

## Description

This function switches from the current schedule table to another one.

By calling this function in the event procedure on preStart, it is possible to specify in which schedule table the measurement should start.

## Parameters

| Name | Description |
|---|---|
| tableIndex | Index of the schedule table to be changed to. Value range: 0..N-1, where N is a total number of defined schedule tables |
| slotIndex | Index of slot to be started within the new schedule table. Default value: 0 Value range: 0..Y-1, where Y is a total number of slots in the new schedule table |
| onSlotIndex | Index of last slot in the current schedule table to be sent before changing to the new schedule table. Default value: -2 - makes change immediately Value range: -2..X-1, where X is a total number of slots in the current schedule table. Value: -1 - makes change on reaching the end of current schedule table. Value: -2 - makes change immediately. |

## Return Values

Index of the current schedule table or -1 if no active schedule table exists and on failure.

## Example

Change to schedule table with index 1 on pressing 'c' key

```c
...
on key 'c'
{
linChangeSchedTable(1);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 3.2 | 3.2 | 13.0 | 13.0 | — | 1.0 |
| Restricted To | LIN | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
