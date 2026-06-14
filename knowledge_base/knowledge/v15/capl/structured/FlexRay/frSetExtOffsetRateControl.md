# frSetExtOffsetRateControl

> Category: `FlexRay` | Type: `function`

## Syntax

```c
int frSetExtOffsetRateControl(int aChannel, int aRateCtrl, int anOffsetCtrl);
```

## Description

Applies the external rate and offset correction values from the FlexRay parameters for the next cycle. For a description and explanation of the external clock correction procedure please refer to the FlexRay specification and/or to the user manual for the E-Ray communication controller.

The function is used in the following sample configuration:

2 Cluster Gateway – FlexRay_2Cluster_Gateway.cfgDemonstrates a FlexRay-FlexRay gateway with manipulation of the routed data and the (optional) synchronization of both FlexRay clusters.

## Parameters

| Name | Description |
|---|---|
| aChannel | FlexRay channel (cluster number) |
| aRateCtrl | Controls whether the rate correction value is to be added, subtracted or ignored: 1: add value -1: substract value 0: ignore value The value referenced is clusterCfg.pExternRateCorrection, which can be read/set by the functions frGetConfiguration and frSetConfiguration. |
| anOffsetCtrl | Controls whether the offset correction value is to be added, subtracted or ignored: 1: add value; -1: substract value; 0: ignore value; The value referenced is clusterCfg.pExternOffsetCorrection, which can be read/set by functions FRGetConfiguration and FRSetConfiguration. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.0 | 6.0 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
