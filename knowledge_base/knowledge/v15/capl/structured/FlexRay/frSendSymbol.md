# frSendSymbol

> Category: `FlexRay` | Type: `function`

## Syntax

```c
frSendSymbol( long <type>, long <param>, int channel );
```

## Description

This function sends an MTS symbol in the next possible symbol window if the Communication Controller is in normal mode (synchronized).

## Parameters

| Name | Description |
|---|---|
| <type> | Not used at this time. Reserved for future expansions. Should always be equal to 0. |
| <param> | Not used at this time. Reserved for future expansions. Should always be equal to 0. |
| channel | Channel number (or cluster number) |

## Return Values

—

## Example

This example sends a MTS symbol when a key is pressed in the next possible cycle.

Note

```c
on key 'm'
{
   frSendSymbol(0 /* not used */, 0 /* not used */, %CHANNEL%);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.0 | 6.0 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
