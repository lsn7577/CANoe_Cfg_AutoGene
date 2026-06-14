# testWaitScopeGetConfigurationInformation

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitScopeGetConfigurationInformation (char deviceNames[][], dword deviceCount, char configurationNames[][], dword configurationCount);
```

## Description

Returns the available oscilloscopes and possible configurations.

The returned device names and function can be used with the function testWaitScopeSetConfiguration.

## Parameters

| Name | Description |
|---|---|
| deviceNames | The names of the scope device. |
| deviceCount | [in] The number of scope devices requested [out] The number of available scope devices |
| configurationNames | The configuration names of all available configurations. |
| configurationCount | [in] The number of requested configurations [out] The number of available configurations |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | — | Scope | Scope | — | — | Scope |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
