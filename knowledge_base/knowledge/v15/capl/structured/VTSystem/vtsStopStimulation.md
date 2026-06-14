# vtsStopStimulation

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsStopStimulation (char Target[]);
```

## Description

Stops the output of a stimulation signal. This resets the stimulation mode. Therefore it is not sufficient to call vtsStartStimulation to start the output again. You also have to restore the stimulation mode, e.g. by calling vtsSetStimulationMode.

At the end of the execution of the command there is a short break before other commands will be executed. This means that the next functions will be executed after a short delay.With this procedure ensures that the stop command is executed effectively. The command should be called only in context of a test module setup but not in handler functions. In handler functions the correct execution of the stop command can not be ensured.

## Parameters

| Name | Description |
|---|---|
| Target | Name of the system variable/namespace that will be affected by this function call. |

## Example

See example vtsSetStimulationMode

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.5 SP2 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | VT offline | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
