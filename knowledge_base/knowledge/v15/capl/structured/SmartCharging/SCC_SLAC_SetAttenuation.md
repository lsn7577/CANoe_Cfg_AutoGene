# SCC_SLAC_SetAttenuation

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SLAC_SetAttenuation ( float AttenuationMean, float AttenuationDev )
```

## Description

Changes the probability distribution used to create attenuation characteristics when simulating a HomePlug Green PHY chip. The values apply to all SLAC sessions, yet may be set each time an M-Sound is received using the indication SCC_CM_MNBC_Sound_Ind.

## Parameters

| Name | Description |
|---|---|
| AttenuationMean | Attenuation Mean Value in dB. |
| AttenuationDev | Standard deviation of the distribution in dB. |

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
