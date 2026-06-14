# DoIP_GetGenericTimeout, DoIP_SetGenericTimeout

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetGenericTimeout( dword toGeneric_ms); // form 1
dword DoIP_GetGenericTimeout(); // form 2
```

## Description

Sets or returns the generic timeout. The generic timeout specifies the maximum time of inactivity of the TCP connection before the connection is automatically closed.

## Parameters

| Name | Description |
|---|---|
| toGeneric_ms | The timeout parameter in milliseconds. |

## Example

This value can also be configured in the DoIP.INI file.

```c
// Set T_TCP_Generic_Inactivity to 30s
DoIP_SetGenericTimeout( 30000);
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
