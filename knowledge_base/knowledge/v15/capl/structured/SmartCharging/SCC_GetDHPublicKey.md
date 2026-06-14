# SCC_GetDHPublicKey

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_GetDHPublicKey ( byte Key[], char IdAttr[] )
```

## Description

Reads the Diffie-Hellman parameter (public key) from a Certificate Installation/Update Response or a Certificate Installation/Update Request (the latter only for versions other than ISO 15118).

## Parameters

| Name | Description |
|---|---|
| Key | Value of element DHPublicKey (ISO 15118) resp. DHParams (other versions). |
| IdAttr | Id attribute of DHPublicKey (ISO 15118 only). |

## Return Values

—

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
