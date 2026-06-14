# sysFilterAddNamespace

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysFilterAddNamespace(char namespace[]); // form 1
long sysFilterAddNamespace(char namespace[], char filterName[]); // form 2
```

## Description

Adds a namespace to the variable filter. If no filterName is given, the namespace is added to the default filter.

## Parameters

| Name | Description |
|---|---|
| namespace | The namespace to add. The existence of the namespace is not checked, and adding a namespace that is not defined is not an error. If the namespace gets defined after it is added to the filter, it is affected by the filter normally. |
| Note An empty filterName refers to the default filter and can be omitted completely. |  |

## Example

```c
long result;
//create the default filter as a Stop Filter
result = sysCreateVariableFilter(0);
//add a namespace to the filter.
result = sysFilterAddNamespace(“myNamespace”);
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
