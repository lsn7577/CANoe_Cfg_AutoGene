# on fct_Returning

> Category: `CommunicationObjects` | Type: `event`

## Description

The event procedure is called when a service function is about to return its answer at a provider. At this time, the automatic answering feature has already set the out parameters and return value to their default values if it is configured and the default answer time has elapsed.

The handler is particularly useful if the answer time is determined by another component.

## Example

```c
on fct_Returning MirrorAdjustment[all,LeftMirror].Adjust
{
  if (abs(this.deltaX) > MAX_X || abs(this.deltaY) > MAX_Y)
  {
    this.Result = Mirrors::AdjustResult::OutOfRange;
  }
  else
  {
    this.Result = Mirrors::AdjustResult::OK;
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | 15 | 14 | 4.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |

## Selectors

| callContext | ../Objects/CAPLfunctionCallContext.htm |
|---|---|
