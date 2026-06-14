# linSetwakeupCondition

> Category: `LIN` | Type: `function`

## Syntax

```c
linSetWakeupCondition(dword numWakeupSignals); // form 1
linSetWakeupCondition(dword numWakeupSignals, dword forgetWupsAfterMS); // form 2
```

## Description

Determines the conditions under which the LIN hardware can be reactivated (leaves the sleep mode).

## Parameters

| Name | Description |
|---|---|
| numWakeupSignals | This parameter specifies the number of wakeup signals, after that the LIN hardware is reactivated. If the value 0 is set, the LIN hardware will never leave the sleep mode. Value range: 0..31 Default value: 1 |
| forgetWupsAfterMS | This parameter defines the time after that earlier wake-up signals are not any longer taken into account for the wake-up behavior. Default value: 0 |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
// configure LIN hardware to wakeup after 3 wakeup signals
linSetWakeupCondition (3);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 8.5 | 13.0 | 13.0 | — | 2.0 |
| Restricted To | LIN | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
