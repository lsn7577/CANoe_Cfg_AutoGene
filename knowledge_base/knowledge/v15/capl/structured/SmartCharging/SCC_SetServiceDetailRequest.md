# SCC_SetServiceDetailRequest

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SetServiceDetailRequest ( dword ServiceId )
```

## Description

Requests the vehicle to send a Service Detail Request during the ServiceDiscoveryRes or ServiceDetailRes callback. It is possible for multiple Service Detail Requests, or none at all, to be sent. If this function is not called, the vehicle skips this message.

## Parameters

| Name | Description |
|---|---|
| ServiceID | ID of service that is to be requested, in hexadecimal representation. |
| ParameterSetID | ID of the desired parameter set (if set to 0, this optional parameter will be omitted). |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | — | — | — | 3.0 SP3 |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | Ethernet .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
