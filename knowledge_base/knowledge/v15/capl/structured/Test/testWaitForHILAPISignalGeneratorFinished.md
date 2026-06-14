# testWaitForHILAPISignalGeneratorFinished

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitForHILAPISignalGeneratorFinished(dword handle);
```

## Description

Waits until a running generator has finished.

## Parameters

| Name | Description |
|---|---|
| handle | Handle of the signal generator that shall be waited for. |

## Example

```c
HILAPIStartSignalGenerator(hGenerator);
testWaitForHILAPISignalGeneratorFinished(hGenerator);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
