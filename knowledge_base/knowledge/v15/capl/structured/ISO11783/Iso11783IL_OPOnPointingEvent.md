# Iso11783IL_OPOnPointingEvent

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783IL_OPOnPointingEvent( long x, long y, dword state );
```

## Description

The function is called by the node layer, if the user clicks into the data mask.

## Parameters

| Name | Description |
|---|---|
| x | X position [pixel] |
| y | Y position [pixel] |
| state | 0: Released (Version ≥ 3) 1: Pressed (pressed) 2: Held (Version ≥ 3) |

## Return Values

—

## Example

```c
void Iso11783IL_OPOnPointingEvent( LONG x, LONG y, dword touchState )
{
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
