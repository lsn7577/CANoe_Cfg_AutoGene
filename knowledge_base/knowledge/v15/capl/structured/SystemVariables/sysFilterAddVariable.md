# sysFilterAddVariable

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysFilterAddVariable(sysVar variable); // form 1
long sysFilterAddVariable(sysVar variable, char filterName[]); // form 2
long sysFilterAddVariable(char namespace[], char variable[]); // form 3
long sysFilterAddVariable(char namespace[], char variable[], char filterName[]); // form 4
```

## Description

Adds a variable to a filter. If no filterName is given, the variable will be added to the default filter.

## Parameters

| Name | Description |
|---|---|
| Note If a struct member is specified, the whole struct will be added. |  |
| Note An empty filterName refers to the default filter and can be omitted completely. |  |
| namespace | The namespace that contains the variable. |
| variable (char[]) | The name of the variable. |

## Example

```c
long result;
//create default filter as Stop Filter
result = sysCreateVariableFilter(0);
//add a variable that should be stopped by the filter
result = sysFilterAddVariable(sysvar::myNamespace::myVariable);
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
