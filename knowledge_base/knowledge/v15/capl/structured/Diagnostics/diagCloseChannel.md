# diagCloseChannel

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagCloseChannel(); // form 1
long DiagCloseChannel(char ecuQualifier[]); // form 2
```

## Description

Closes a diagnostic channel. State of the channel is Closed afterwards.

The channel the function refers to is set with the last call of diagSetTarget.

## Parameters

| Name | Description |
|---|---|
| ecuQualifier | Qualifier of the ECU or target as set in the diagnostic configuration dialog for the respective diagnostic description. |

## Return Values

On success 0, otherwise error code.

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
