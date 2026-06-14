# diagIsChannelConnected

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagIsChannelConnected(); // form 1
long DiagIsChannelConnected(char ecuQualifier[]); // form 2
```

## Description

Checks if a channel is already in state Connected.

The channel the function refers to is set with the last call of diagSetTarget.

## Parameters

| Name | Description |
|---|---|
| ecuQualifier | Qualifier of the ECU or target as set in the diagnostic configuration dialog for the respective diagnostic description. |

## Return Values

1 if channel is connected, 0 if channel is not connected, otherwise error code.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0: form 1 9.0 SP3: form 2 | 8.0: form 1 9.0 SP3: form 2 | — | — | — | 1.0: form 1 2.1 SP3: form 2 |
| Restricted To | Real bus mode Online mode | Real bus mode Online mode | — | — | — | Real bus mode Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
