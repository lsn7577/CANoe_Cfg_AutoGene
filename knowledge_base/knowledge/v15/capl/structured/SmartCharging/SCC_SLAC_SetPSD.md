# SCC_SLAC_SetPSD

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
SCC_SLAC_SetPSD ( byte PSD[] )
```

## Description

Fills the power spectral density map as a prerequisite for Amplitude Map Exchange. The data format is equal to the message CM_SLAC_AmpMap.Req, so the data will be sent exactly as set with this function.

To deactivate Amplitude Map Exchange (default), set a map of {0..0} .

To activate Amplitude Map Exchange, set a map that contains values != 0 .

Note: Because the PSD is defined in values of 4 bit, only the lower half of each byte is considered.

## Parameters

| Name | Description |
|---|---|
| PSD | 58 byte Power Spectral Density in differences to the specified mean value and in [-dBm/Hz]. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | — | — | — | 4.0 |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | Ethernet .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
