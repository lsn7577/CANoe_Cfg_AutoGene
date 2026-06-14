# sysGetVariableLongLong

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
int64 sysGetVariableLongLong(char namespace[], char variable[]); // form 1
int64 sysGetVariableLongLong(SysVarName); // form 2
long sysGetVariableLongLong(char namespace[], char variable[], int64& value); // form 3
long sysGetVariableLongLong(SysVarName, int64& value); // form 4
```

## Description

Returns the value of a variable of a 64 bit integer type.

## Parameters

| Name | Description |
|---|---|
| namespace | Name of the name space. |
| variable | Name of the variable. |
| value | Receives the current value of the variable. |
| SysVarName | Name of the fully qualified name of the system variable, including all name spaces, separated by "::". The name must be preceded by "sysVar::". |

## Return Values

Value of the variable or 0 in case of error (form 1 and 2)

## Example

```c
sysGetVariableLongLong(sysvar::MyNamespace::Int64Var);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 8.5 | 13.0 | 13.0: form 2 | 14 | 2.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
