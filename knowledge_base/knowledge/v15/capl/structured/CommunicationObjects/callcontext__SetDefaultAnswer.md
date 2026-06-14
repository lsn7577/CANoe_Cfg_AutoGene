# callcontext::SetDefaultAnswer

> Category: `CommunicationObjects` | Type: `method`

## Syntax

```c
void callContext::SetDefaultAnswer();
```

## Description

Sets the return value and the out parameters for the call to their defaults.

The values are set to their defaults on receival of a call if the AutoAnswerMode is set to Auto. You can (re)set them explicitly with this method.

You can change the defaults with the ParamDefaults and DefaultResult properties at the provider endpoint.

## Return Values

—

## Example

```c
on fct_Called MirrorAdjustment.providerSide[all,LeftMirror].Adjust
{
  this.SetDefaultAnswer();
  this.SetTimeToAnswer(10);
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
