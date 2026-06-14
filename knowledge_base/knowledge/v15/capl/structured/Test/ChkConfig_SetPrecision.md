# ChkConfig_SetPrecision

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkConfig_SetPrecision(unsigned int aPrecision);
```

## Description

This function configures the TSL time basis for the current node. The time basis (precision) affects all future times that are passed when creating checks (see check descriptions), and it affects the time basis for queries (status report functions).

This function allows you to configure the time basis for new checks to be created.The time bases of checks that have already been created are not changed by this function. They can be polled by a special query.

## Parameters

| Name | Description |
|---|---|
| 3 | 10 –3 seconds = ms (default) |
| 4 | 10 –4 seconds |
| 5 | 10 –5 seconds = 10 us: e.g. used in trace export |
| 6 | 10 –6 seconds = us |
| 7 | 10 –7 seconds |
| 8 | 10 –8 seconds |
| 9 | 10 –9 seconds = ns |

## Example

```c
// precision of the test is set to us
chkConfig_SetPrecision(6);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
