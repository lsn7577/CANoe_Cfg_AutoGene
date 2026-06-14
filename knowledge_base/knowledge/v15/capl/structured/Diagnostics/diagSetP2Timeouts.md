# diagSetP2Timeouts

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagSetP2Timeouts( dword newP2timeout_ms, dword newP2exTimeout_ms); // form 1
long DiagSetP2Timeouts(char ecuQualifier[], dword P2Timeout_ms , dword P2exTimeout_ms); // form 2
```

## Description

Changes the P2 and P2ex timeout values at the built-in diagnostic channel.

## Parameters

| Name | Description |
|---|---|
| newP2timeout_ms | The built-in diagnostic channel will use this P2 timeout (in milliseconds) from now on. |
| newP2exTimeout_ms | New P2 extended value (in milliseconds) for the built-in diagnostic channel. |
| ecuQualifier | Qualifier of the ECU or target as set in the diagnostic configuration dialog for the respective diagnostic description. |

## Return Values

-1 for failed or error code.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2: form 1 9.0 SP3: form 2 | 7.0 SP4: form 1 9.0 SP3: form 2 | — | — | — | 1.0: form 1 2.1 SP3: form 2 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
