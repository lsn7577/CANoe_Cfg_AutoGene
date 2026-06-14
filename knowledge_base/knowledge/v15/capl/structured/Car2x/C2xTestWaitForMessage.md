# C2xTestWaitForMessage

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xTestWaitForMessage(char* appMsg, long aTimeout) // form 1
long C2xTestWaitForMessage(char* appMsg, char* stationName, long aTimeout) // form 2
```

## Description

Waits for the occurrence of the first Car2x message matching the conditions passed as arguments. Should the message not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

## Parameters

| Name | Description |
|---|---|
| appMsg | Name of application message of the Car2x message that should be awaited. |
| stationName | Name of the sender station of the Car2x message that should be awaited. |
| aTimeout | Maximum time that should be waited [ms]. Transmission of 0: no timeout controlling |

## Example

```c
long result;
//Form 1: Wait for occurrence of Car2x message with application message "CAM"
result = C2xTestWaitForMessage("CAM", 1000);

//Form 2: Wait for occurrence of Car2x message with application message "CAM" and sender "Staion1"
result = C2xTestWaitForMessage("CAM", "Station1", 1000);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0: form 1, 2 | — | — | — | 5.0: form 1, 2 |
| Restricted To | — | Car2x, Testnodes: form 1, 2 | — | — | — | Car2x: form 1, 2 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
