# mostPMTempShutdownWakeupTimeout

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostPMTempShutdownWakeupTimeout (long timeout);
```

## Description

As described in the MOST specification in the chapter "Over-Temperature Management", the PowerMaster may try to wake-up the MOST ring, after a temperature shutdown, after a certain time. This function sets the timeout duration.

The default value is 60s.

## Parameters

| Name | Description |
|---|---|
| timeout | Timeout in [ms]. |

## Return Values

See error codes

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | — | — | — | —✔ |
| Restricted To | — | MOST25 MOST50 MOST150 While Application Socket is active Only in device with MOST PowerMaster | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | — | ✔ | — | — | — | —✔ |
