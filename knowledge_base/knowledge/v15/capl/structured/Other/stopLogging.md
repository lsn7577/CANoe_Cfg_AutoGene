# stopLogging

> Category: `Other` | Type: `function`

## Syntax

```c
void stopLogging(); // from 1
void stopLogging(char strLoggingBlockName[]); // from 2
void stopLogging(char strLoggingBlockName[], long postTriggerTime); // from 3
```

## Description

Stops all Logging Blocks immediately bypassing all logging trigger settings.

Stops a Logging Block with name strLoggingBlockName immediately bypassing all logging trigger settings.

Stops a Logging Block with name strLoggingBlockName bypassing all logging trigger settings.

Functions also sets a post-trigger time to a value of the postTriggerTime.

## Parameters

| Name | Description |
|---|---|
| Note If you use the function in standalone mode and if you activated logging and Trigger Block in the standalone mode configuration settings you can address the (single) Logging Block available in this case by passing an empty string as parameter. |  |
| postTriggerTime | Post-trigger time interval in ms. |

## Return Values

—

## Example

```c
startLogging();
// starts all Logging Blocks
stopLogging();
// stops all Logging Blocks
startLogging( "Logging 1");
// starts the Logging Block "Logging 1"
stopLogging( "Logging 1");
// stops the Logging Block "Logging 1"
startLogging( "Logging 1", 2000);
// starts the Logging Block "Logging 1" with pre-trigger time 2000 milliseconds.
stopLogging( "Logging 1", 1000);
// stops the Logging Block "Logging 1" with post-trigger time 1000 milliseconds.
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 4.1 | 4.1 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
