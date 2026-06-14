# FDXSetByteOrder

> Category: `Other` | Type: `function`

## Syntax

```c
long FDXSetByteOrder(long fdxClientHandle, long byteOrder);
```

## Description

This function configures the byte order of the FDX protocol that should be used for the communication with the specified client. The default is Little Endian.

## Parameters

| Name | Description |
|---|---|
| fdxClientHandle | FDX client for which the byte order should be set. |
| byteOrder | 1: Little Endian 2: Big Endian |

## Example

Coupling of two CANoe Instances using the FDX Protocol

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 SP3 | 13.0 | — | 14 | 2.2 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
