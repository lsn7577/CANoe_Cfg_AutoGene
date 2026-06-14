# lookupSysvar

> Category: `Other` | Type: `function`

## Syntax

```c
sysvar * lookupSysvar(char sysvarName[]); // form 1
sysvar * lookupSysvar(char namespace[], char variable[]); // form 2
```

## Description

Searches for a system variable definition. If the system variable is not found, test modules/units report an error in test system while simulation/analysis nodes write a warning into the Write Window, and the function returns an invalid sysvar.

## Parameters

| Name | Description |
|---|---|
| sysvarName | Fully qualified name of the variable (including namespaces) |
| namespace | Namespace(s) of the variable, separated with :: |
| variable | Name of the variable |

## Return Values

The found system variable or an invalid object.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 | 10.0 | 13.0 | 13.0 | 14 | 2.2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
