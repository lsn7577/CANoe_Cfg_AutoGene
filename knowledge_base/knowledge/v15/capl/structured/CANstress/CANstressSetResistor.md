# CANstressSetResistor

> Category: `CANstress` | Type: `function`

## Syntax

```c
void CANstressSetResistor (dword resId, float value);
```

## Description

Sets the value of a resistor for analog disturbances. This command will only take effect if permitted by the resistor layout set in the basic configuration. If the R_H layout is active, it will only be possible to set the RH resistor. If the CANstress device is inactive at this point, settings will only be applied once the CANstress device is active, i.e., once the trigger has been activated.

## Parameters

| Name | Description |
|---|---|
| 1 | for RH |
| 2 | for RSH |
| 3 | for RHL |
| 4 | for RSL |
| 5 | for RL |
| value | New resistor value. The value is specified in ohms, whereby only multiples of 2.5 in the range between 0 and 10,237.5 are valid. In the event of values that may be invalid, a warning will appear in the test report. If an invalid value is transferred, it will be ignored (i.e., not applied) by the COM server. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | — | — | — | 1.1 |
| Restricted To | — | CAN CANstress | — | — | — | CAN CANstress |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
