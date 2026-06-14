# GPIBOnError

> Category: `GPIB` | Type: `function`

## Syntax

```c
GPIBOnError (long deviceDescriptor, char query[], char response[], long status, long error);
```

## Description

This optional function is called if a query or a write operation (GPIBWriteStr or GPIBWriteNum) raised an error condition.

Users may implement this function and then receive the original query string or the data to be written, respectively. The result string, if any, is also returned, as well as the GPIB status word, the error code and the device descriptor.

## Parameters

| Name | Description |
|---|---|
| deviceDescriptor | The descriptor of the device that transmitted the response. |
| query | The data transmitted in the failed GPIBQuery… or GPIBWrite… call, respectively |
| response | The data received from the device so far. The empty string if a write operation failure is reported. |
| status | The GPIB status word. |
| error | The GPIB error code. |

## Return Values

—

## Example

The GPIBOnError callback function is used very much like GPIBResponse. Refere to it for an example.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 SP4 | — | — | — | 1.1 SP2 |
| Restricted To | — | GPIB | — | — | — | GPIB |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
