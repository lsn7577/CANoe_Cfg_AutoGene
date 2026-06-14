# sysFilterRemoveNamespace

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysFilterRemoveNamespace(char namespace[]); // form 1
long sysFilterRemoveNamespace(char namespace[], char filterName[]); // form 2
```

## Description

Removes a namespace from the variable filter. If no filterName is given, the namespace is removed from the default filter.

## Parameters

| Name | Description |
|---|---|
| namespace | The namespace to remove. |
| Note An empty filterName refers to the default filter and can be omitted completely. |  |

## Example

```c
long result;
//remove a namespace from the default filter.
result = sysFilterRemoveNamespace(“myNamespace”);
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
