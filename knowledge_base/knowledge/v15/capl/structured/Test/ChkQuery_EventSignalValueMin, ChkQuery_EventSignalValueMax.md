# ChkQuery_EventSignalValueMin, ChkQuery_EventSignalValueMax

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_EventSignalValueMin(dword checkId, int64& value);
long ChkQuery_EventSignalValueMax(dword checkId, int64& value);
long ChkQuery_EventSignalValueMin(dword checkId, double& value);
long ChkQuery_EventSignalValueMax(dword checkId, double& value);
```

## Description

Enables access to the minimal and maximal measured values within a check.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Example

```c
double maxValue;
int checkId;

checkId = ChkStart_MsgSignalValueInvalid (singalToObserve, 5.5, 10.5);    TestAddCondition(checkId)
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
ChkQuery_EventSignalValueMax(checkID, maxValue);

write("Max signal value=%f", maxValue);

TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | 13.0 | — | 14 | 2.1 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
