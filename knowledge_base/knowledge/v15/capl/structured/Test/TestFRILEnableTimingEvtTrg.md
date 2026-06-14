# TestFRILEnableTimingEvtTrg

> Category: `Test` | Type: `function`

## Syntax

```c
long TestFRILEnableTimingEvtTrg(char pduName[], int enable);
```

## Description

Controls the event triggered timing of PDUs. The event triggered timing can be enabled/ disabled.

This function influences a simulation node with an assigned CANoe Interaction Layer.

## Parameters

| Name | Description |
|---|---|
| aPDUName | Name of the PDU that should be modified. |
| enable | 0 = disable1 = enable |

## Example

```c
int enable;
.....
If( stopEvtSending == 1 )
{
   enable = 0;
}
else
{
   enable = 1;
}
TestFRILEnableTimingEvtTrg (pduXY, enable);
.....
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6 SP4 | 13.0 | — | — | 1.0 |
| Restricted To | — | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
