# sysIsVariableTypeSigned

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
dword sysIsVariableTypeSigned(sysvar * variable);
```

## Description

Returns whether the data type of the system variable is a signed numeric type. The function returns 1 for system variables of type Int64, Int32, Double, Integer Array and Double Array. It returns 0 for other variables, in particular for variables of type UInt32 and UInt64.

## Parameters

| Name | Description |
|---|---|
| variable | the variable |

## Example

```c
sysvar * var;
var = lookupSysvar("SomeNamespace::SomeVariable");
write("Signed: %d", sysIsVariableTypeSigned(var));
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 13.0 SP2 | 13.0 SP2 | 13.0 | — | 14 |  |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
