# sysSetVariableFilterActive

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysSetVariableFilterActive(dword active); // form 1
long sysSetVariableFilterActive(dword active, char filterName[]); // form 2
```

## Description

Activates or deactivates a variable filter. If no filterName is given, the default filter is affected.

## Parameters

| Name | Description |
|---|---|
| active | Specifies the new filter status: 0: deactivated. All other values: activated. |
| Note An empty filterName refers to the default filter and can be omitted completely. |  |

## Example

```c
long result;
//create the default filter as a Stop Filter.
result = sysCreateVariableFilter(0);
//deactivate the default filter.
result = sysSetVariableFilterActive(0);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.1 | 8.1 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ (also standalone mode) | ✔ (also standalone mode) | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | ✔ | — | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
