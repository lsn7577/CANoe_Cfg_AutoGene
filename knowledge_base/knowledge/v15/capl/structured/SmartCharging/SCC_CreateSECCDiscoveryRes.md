# SCC_CreateSECCDiscoveryRes

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_CreateSECCDiscoveryRes ( char IpAddress [],dword Port, dword TLSEnabled) //form 1
long SCC_CreateSECCDiscoveryRes ( char IpAddress [], dword Port, dword Security, dword TransportProtocol ) //form 2
```

## Description

Creates a SECC Discovery Response message for sending.

Form 1 creates valid messages only.

Form 2 allows to specify arbitrary byte values for the two message parameters Security and TransportProtocol.

## Parameters

| Name | Description |
|---|---|
| IpAddress | String representation of the EVSE’s IPv6 address in the usual notation. |
| Port | Target port number. |
| TLSEnabled | 1 for TLS, 0 for no transport layer security. |
| Security | Security field (1 byte), valid values: 0x00 = TLS, 0x10 = No transport layer security. |
| TransportProtocol | Transport protocol field (1 byte), valid values: 0x00 = TCP. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3: form 1 13.0: form 2 | — | — | — | 3.0 SP3: form 1 5.0: form 2 |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | Ethernet .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
