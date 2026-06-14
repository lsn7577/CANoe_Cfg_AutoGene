# OnMostMHPError

> Category: `MOST` | Type: `function`

## Syntax

```c
long OnMostMHPError(long sourceDevID, long destDevID, long fBlockID, long instID, long functionID, long opType);
```

## Description

The event procedure is called up as soon as a MOST High protocol violation is observed.

Within this event procedure the following functions are available

Indicates the MHP observer error number. See possible MHP observer error codes.Parameter:NoneReturns: Observer error number

Indicates the error value. Not supported by all error codes.Parameter:NoneReturns: Error value or 0

Indicates the expected value. Not supported by all error codes.Parameter:NoneReturns: Expected value or 0

Indicates if this is a warning. Warnings may indicate a communication problem.Parameter:NoneReturns: Error value or 0

The functions mostEventChannel, mostEventTime and mostEventTimeNS can be used to call up supplemental information.

## Parameters

| Name | Description |
|---|---|
| sourceDevID | Address of the transmitter |
| destDevID | Address of the receiver |
| fBlockID | FBlockID of the receiver |
| instID | Instance ID of the receiver |
| functionID | FunctionID of the receiver |
| opType | OpType of the receiver |

## Return Values

The return value determines whether the MHP error event is relayed to the next function block in the Measurement Setup (e.g. a Trace Window).

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.0 | 6.0 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | — | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | — | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | —✔ |
| 32-Bit | — | — | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
