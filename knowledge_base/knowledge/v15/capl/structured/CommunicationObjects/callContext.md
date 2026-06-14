# callContext

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
callContext * <var>; // form 1
callContext <Method> <var>; // form 2
callContext <Prototype> <var>; // form 3
```

## Description

Contains data of a function call, in particular the parameter values.

## Parameters

| Name | Description |
|---|---|
| Method | Method of a service, determining the data type of the call |
| Prototype | Function prototype (signature), determining the data type of the call |

## Example

```c
variables
{
  callContext MirrorAdjustment.Adjust deferredAnswer;
}

on fct_Calling MirrorAdjustment[all, LeftMirror].Adjust
{
  this.DeferAnswer();
  deferredAnswer = this;
}

on sysvar Panels::ReturnAnswer
{
  deferredAnswer.ReturnCall(Mirrors::AdjustResult::OK);
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
