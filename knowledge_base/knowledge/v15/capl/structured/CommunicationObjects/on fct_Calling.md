# on fct_Calling

> Category: `CommunicationObjects` | Type: `event`

## Description

The event procedure is called when a service function is about to be called at a provider. At this time, the automatic answering feature has not yet set out parameters or delay, so you can still use the ParamDefaults or DefaultResult values to configure it.

## Example

```c
on fct_Calling MirrorAdjustment[all,LeftMirror].Adjust
{
  if (abs(this.deltaX) > MAX_X || abs(this.deltaY) > MAX_Y)
  {
    $MirrorAdjustment.providerSide[all,LeftMirror].Adjust.DefaultResult = Mirrors::AdjustResult::OutOfRange;
  }
  else
  {
    $MirrorAdjustment.providerSide[all,LeftMirror].Adjust.DefaultResult = Mirrors::AdjustResult::OK;
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
