# coTfsSetTimeoutValue

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSetTimeoutValue( dword timeout );
```

## Description

This function sets the general time-out of all test functions, insofar as individual functions do not make a separate parameter available for this. The default value at measurement start is 2500 ms. If the value is set to 0, the function waits endlessly.

## Parameters

| Name | Description |
|---|---|
| timeout | Time-out in ms. |

## Return Values

Error code

## Example

```c
coTfsSetTimeoutValue (300); // set time-out to 300 ms
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
