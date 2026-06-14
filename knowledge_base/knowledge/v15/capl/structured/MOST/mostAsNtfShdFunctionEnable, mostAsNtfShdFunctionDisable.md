# mostAsNtfShdFunctionEnable, mostAsNtfShdFunctionDisable

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsNtfShdFunctionEnable(long fblockId, long instId, long functionId);
long mostAsNtfShdFunctionDisable(long fblockId, long instId, long functionId);
```

## Description

mostAsNtfShdFunctionEnable() registers a MOST function with the notification shadow service. As soon as the specified function block (fblockId, instId) appears in the bus registry of the simulated device, the notification shadow service enters the simulated device in the notification matrix of the function block, i.e., it sends the FBlockId.InstId.Notification.Set(SetFunction, functionId) message.

mostAsNtfShdFunctionDisable() removes a MOST function from the notification shadow service.

## Parameters

| Name | Description |
|---|---|
| fblockId | Function block ID |
| instId | Instance ID |
| functionId | Function ID of a "Property" type function. |

## Return Values

See error codes

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | — | — | — | —✔ |
| Restricted To | — | MOST25 MOST50 MOST150 While Application Socket is active | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | — | ✔ | — | — | — | —✔ |
