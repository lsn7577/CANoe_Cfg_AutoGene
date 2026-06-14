# linRunSchedTableNtimes

> Category: `LIN` | Type: `function`

## Syntax

```c
long linRunSchedTableNtimes (dword tableIndex, dword numberOfRepetitions, dword onSlotIndex, dword returnToTableIndex);
```

## Description

Switches from the current schedule table to another one, runs the table n times and returns to the initial table or to a different table.

## Parameters

| Name | Description |
|---|---|
| tableIndex | Index of the schedule table to be changed to. Value range: 0..n-1, where n is a total number of defined schedule tables |
| numberOfRepetitons | Number of repetitions of the schedule table. |
| onSlotIndex | Index of last slot in the current schedule table to be sent before changing to the new schedule table. Default value: -1, make change on reaching the end of current schedule table. Value range: -1..x-1, where x is a total number of slots in the current schedule table. |
| returnToTableIndex | Default value: -1, return to previous table. Value range: 0..n-1, where n is a total number of defined schedule tables. |

## Return Values

Index of the current schedule table or -1 if no active schedule table exists and on failure.

## Example

```c
// on pressing key ‘c’ change to schedule table with index 1, run it 2 times and return to the previous table
...
on key 'c'
{
  linRunSchedTableNTimes (1, 2, -2, -1);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.2 | 8.2 | — | 13.0 | — | 1.1 |
| Restricted To | LIN | LIN | — | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | ✔ | — | N/A |
