# J1939TestStmControl_Start

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestStmControl_Start( long stimulusId );
```

## Description

Starts or continues sending a Stimulus Parameter Group. May work on a Stimulus stopped earlier, or on a Stimulus created in previously. Ignored for active Stimuli.

## Parameters

| Name | Description |
|---|---|
| stimulusId | identifier of the Stimulus to start |

## Example

```c
long toggleStm;
pg MyPG myPG;

myPG.SA = 1;
myPG.DA = 2;

toggleStm = J1939TestStmCreate_Toggle( myPG, MyPg::SignalA, 100, 10, 20 );
J1939TestStmControl_Start(toggleStm);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 | 13.0 | — | — | 1.1 SP2 |
| Restricted To | — | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
