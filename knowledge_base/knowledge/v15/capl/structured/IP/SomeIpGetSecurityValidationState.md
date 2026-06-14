# SomeIpGetSecurityValidationState

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpGetSecurityValidationState ( dword messageHandle );
```

## Description

This function returns the Security-Validation-State of a received SOME/IP message.

## Parameters

| Name | Description |
|---|---|
| messageHandle | Handle of a received SOME/IP message (e.g. see OnSomeIpMessage) |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 SP4 | 10.0 SP4 | — | — | — | —✔ |
| Restricted To | Ethernet | Ethernet | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
