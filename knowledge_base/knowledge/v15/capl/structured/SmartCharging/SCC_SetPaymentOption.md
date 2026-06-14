# SCC_SetPaymentOption

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SetPaymentOption ( char PaymentOption[], dword Force )
```

## Description

Sets the desired payment option for a running SCC session.

## Parameters

| Name | Description |
|---|---|
| PaymentOption | Desired payment option as string. For ISO 15118, the value must be either Contract (indicates PnC mode) or ExternalPayment (indicates EIM mode). |
| Force | If set to 1, the vehicle is forced to set the payment option even if the charge point hasn’t offered it previously. If set to 0, the payment option is only selected if it has been offered. |

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
