# diagGetP6Extended, diagGetP6Timeout, diagSetP6Timeouts

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DiagGetP6Extended(dword source);
long DiagGetP6Extended(char ecuQualifier[], dword source);
long DiagGetP6Timeout(dword source);
long DiagGetP6Timeout(char ecuQualifier[], dword source);
long DiagSetP6Timeouts(dword newP6_ms, dword newP6ex_ms);
long DiagSetP6Timeouts(char ecuQualifier[], dword newP6_ms, dword newP6ex_ms);
```

## Description

Returns or sets the time P6 and P6ex (in milliseconds) from the given source.

If an ECU qualifier is given, the build-in communications channel for this target is accessed.

When a Diagnostics over IP target is active, the P2 timeouts cannot be used because a TCP/IP connection does not provide end of transmission and start of reception events. Therefore the P2 functionality cannot be implemented and the overall timeout P6 has been defined.

## Parameters

| Name | Description |
|---|---|
| Value | Description |
| 0 | Currently active value, i.e. the value originally set or last set from CAPL |
| 1 | Value stored at the selected interface in the description's document |
| 2 | Value configured in the configuration dialog for the description |
| other | reserved |
| Note Basic diagnostic devices do not have an interface defined in a description, therefore source=1 will return the value set at the configuration (source=2). |  |
| ecuQualifier | Qualifier of the ECU or target as set in the diagnostic configuration dialog for the respective diagnostic description. |
| newP6_ms, newP6ex_ms | The DTL diagnostics communication channel uses these timeouts (in milliseconds) from now on. |

## Return Values

Error code

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 | 9.0 | — | — | — | 2.1 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
