# SCC_SendPreparedMessage

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SendPreparedMessage ( ) // form 1
long SCC_SendPreparedMessage ( dword ConfigSection ) //form 2
```

## Description

Sends a message created using one of the Create-functions. Use the function call with parameter ConfigSection to create a signed message using the certificate name from the XML config. Else an unsigned message is sent.

## Parameters

| Name | Description |
|---|---|
| ConfigSection | ID of the config section where the certificates can be found. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3: form 1, 2 | — | — | — | 3.0 SP3: form 1, 2 |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | Ethernet .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
