# linGetRespError

> Category: `LIN` | Type: `function`

## Syntax

```c
long linGetRespError(); // form 1
long linGetRespError(long NAD); // form 2
```

## Description

With this function it’s possible to query the response error flag of the calling Slave node or of the Slave node specified by its node address (NAD) as last seen on the LIN bus.

## Parameters

| Name | Description |
|---|---|
| NAD | Configured node address of the Slave node to be queried. |

## Return Values

Returns one if the queried response_error flag is set, zero if it is not set and -1 if it has not been sent yet.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | 13.0 | 13.0 | — | 1.0 |
| Restricted To | — | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
