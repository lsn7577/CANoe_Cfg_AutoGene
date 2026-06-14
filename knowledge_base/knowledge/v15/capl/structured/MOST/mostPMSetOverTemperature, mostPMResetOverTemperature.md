# mostPMSetOverTemperature, mostPMResetOverTemperature

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostPMSetOverTemperature ();
long mostPMResetOverTemperature ();
```

## Description

mostPMSetOverTemperature notifies the PowerMaster in its own device that an over temperature of the device will be simulated. When setting the "over temperature status", the PowerMaster is prompted to not wake-up the ring after it has been shut down, if a MOST signal is detected at the Rx FOT.mostPMResetOverTemperature signals the PowerMaster that the device has again reached operating temperature.

## Return Values

See error codes

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | — | — | — | —✔ |
| Restricted To | — | MOST25 MOST50 MOST150 While Application Socket is active Only in device with MOST PowerMaster | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | — | ✔ | — | — | — | —✔ |
