# CreateGlobalMarker

> Category: `Other` | Type: `function`

## Syntax

```c
long createGlobalMarker (char markerName[], char makerDesc []);
```

## Description

Sets a marker in CANoe Trace Window, Graphics Window and State Tracker. The set marker can be displayed with the shortcut menu Show in the marker bar of these windows.

## Parameters

| Name | Description |
|---|---|
| markerName | Name of the marker. |
| makerDesc | Description of the marker. |

## Return Values

—

## Example

```c
on key 'a'
// sets a marker by pressing key <a>
{
  createGlobalMarker("speed", "speedDesc");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.1 | 8.1 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | — | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
