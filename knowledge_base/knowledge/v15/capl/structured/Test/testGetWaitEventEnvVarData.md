# testGetWaitEventEnvVarData

> Category: `Test` | Type: `function`

## Syntax

```c
long testGetWaitEventEnvVarData(dword index, float & value); // form 1
long testGetWaitEventEnvVarData(dword index, char value[], dword length); // form 2
long testGetWaitEventEnvVarData(dword index, byte value[], dword length); // form 3
```

## Description

Retrieves the environment variable value that has led to the resume of a joined wait statement.

## Parameters

| Name | Description |
|---|---|
| value | The variable will be filled with the current value of the environment variable value. |
| length | Length of the char or byte filled. Used for environment variables of type string and data. |
| index | Number of the "joined event" corresponds with the return value of "testJoin...". |

## Example

```c
// add envVar event to the current set of “joined events” and get the envVar value
dword index = 0;
float evValue = 0;
TestJoinEnvVarEvent(MyEnvVar);
// ... other join events
index = TestWaitForAnyJoinedEvent(2000);

TestGetWaitEventEnvVarData(index, evValue);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0: form 1-3 8.5 SP3: form 4 | 13.0 | — | — | 1.0: form 1-3 2.0 SP2: form 4 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
