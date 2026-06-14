# DoIP_GetDiagnosticMessageTimeout, DoIP_SetDiagnosticMessageTimeout

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetDiagnosticMessageTimeout(dword toDiagnosticMessage);
dword DoIP_GetDiagnosticMessageTimeout();
```

## Description

Sets or returns the timeout waiting for a diagnostic message positive or negative acknowledgment.

## Parameters

| Name | Description |
|---|---|
| toDiagnosticMessage | An ACK is expected within this amount of milliseconds [ms]. |

## Example

This value can also be configured in the DoIP.INI file.

```c
// Expect an ACK within 1 second
DoIP_SetDiagnosticMessageTimeout(1000);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP4 | — | — | — | 1.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
