# linActivateSlot

> Category: `LIN` | Type: `function`

## Syntax

```c
long linActivateSlot(dword tableIndex, dword slotIndex);
```

## Description

Reactivates a schedule table slot defined in the LIN database file (LDF), after having been previously deactivated by linDeactivateSlot().

Schedule slots containing MasterRequests are automatically sent only if their data is updated i.e. using output().

## Parameters

| Name | Description |
|---|---|
| tableIndex | Schedule table index according to the LIN database file (LDF). First table in the LDF has the index 0. |
| slotIndex | Slot index. First slot in a table has the index 0. |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.1 | 5.1 | 13.0 | 13.0 | — | 1.0 |
| Restricted To | LIN | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
