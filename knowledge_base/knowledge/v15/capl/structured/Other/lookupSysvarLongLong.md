# lookupSysvarLongLong

> Category: `Other` | Type: `function`

## Syntax

```c
sysvarLongLong * lookupSysvarLongLong(char sysvarPath[]); // form 1
sysvarLongLong * lookupSysvarLongLong(char namespace[], char sysvarName[]); // form 2
```

## Description

Searches for a system variable definition. If the system variable is not found or has a wrong type, test modules/units report an error in test system while simulation/analysis nodes write a warning into the Write Window, and the function returns an invalid sysvar.

## Parameters

| Name | Description |
|---|---|
| sysvarPath | Fully qualified name of the variable (including namespaces) |
| namespace | Namespace(s) of the variable, separated with :: |
| sysvarName | Name of the variable |

## Return Values

The found system variable or an invalid object.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 | 10.0 | 13.0 | — | 14 | 2.2 |
| Restricted To | CAN | CAN | CAN | — | CAN | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
