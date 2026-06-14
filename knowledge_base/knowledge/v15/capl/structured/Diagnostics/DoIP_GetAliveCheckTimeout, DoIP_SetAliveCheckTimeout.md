# DoIP_GetAliveCheckTimeout, DoIP_SetAliveCheckTimeout

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetAliveCheckTimeout(dword toAliveCheck_ms);
dword DoIP_GetAliveCheckTimeout();
```

## Description

Sets or returns Alive Check Timeout (T_TCP_Alive_Check)) in milliseconds.

This function must be called in on preStart.

## Parameters

| Name | Description |
|---|---|
| toAliveCheck_ms | The timeout parameter in milliseconds. |

## Example

This value can also be configured in the DoIP.INI file.

```c
// Set T_TCP_Alive_Check to 3s
DoIP_SetAliveCheckTimeout( 3000);
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
