# DoIP_GetInitialTimeout, DoIP_SetInitialTimeout

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetInitialTimeout( dword toInitial_ms); // form 1
dword DoIP_GetInitialTimeout(); // form 2
```

## Description

Sets or returns the initial timeout, started when a tester connects to the ECU (in milliseconds). A route activation request must be received in this interval, otherwise the TCP connection is closed.

## Parameters

| Name | Description |
|---|---|
| toInitial_ms | The timeout parameter in milliseconds. |

## Example

This value can also be configured in the DoIP.INI file.

```c
// Set T_TCP_Initial_Inactivity to 3s
DoIP_SetInitialTimeout( 3000);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 SP4: form 1 8.1 SP4: form 2 | — | — | — | 1.0: form 1 1.0 SP2: form 2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
