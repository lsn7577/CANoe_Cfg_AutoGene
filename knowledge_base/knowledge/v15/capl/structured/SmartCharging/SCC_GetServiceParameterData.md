# SCC_GetServiceParameterData

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_GetServiceParameterData ( long i1, long i2, char Name[], char ValueType[] )
```

## Description

Gets the name and value type of the parameter with the selected indices.

## Return Values

The name and value type of the parameter with the selected indices, where the following applies:
For DIN 70121, ValueType is the actual content of the element <ValueType>. For ISO 15118, the subelement holding the parameter value is evaluated and ValueType is set accordingly. In both cases, there are the same possible results for ValueType, e.g. int, physicalValue, string.

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
