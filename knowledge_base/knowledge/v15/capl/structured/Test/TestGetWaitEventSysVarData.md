# TestGetWaitEventSysVarData

> Category: `Test` | Type: `function`

## Syntax

```c
long testGetWaitEventSysVarData(dword index, float & value); // form 1
long testGetWaitEventSysVarData(dword index, char value[], dword length); // form 2
long testGetWaitEventSysVarData(dword index, float value[], dword length); // form 3
long testGetWaitEventSysVarData(dword index, int64 & value); // form 4
```

## Description

Retrieves the system variable value that has led to the resume of a joined wait statement.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Example

```c
// add sysVar event to the current set of “joined events” and get the sysVar value
dword index = 0;
float sysValue = 0;
TestJoinSysVarEvent(MySysVar);
// ... other join events
index = TestWaitForAnyJoinedEvent(2000);

TestGetWaitEventSysVarData(index, sysValue);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
