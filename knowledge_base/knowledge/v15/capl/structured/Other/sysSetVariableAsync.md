# sysSetVariableAsync

> Category: `Other` | Type: `function`

## Syntax

```c
void sysSetVariableAsync(SysVarName, byte data[], long size); // form 1
void sysSetVariableAsync(SysVarName, float value); // form 2
void sysSetVariableAsync(SysVarName, float values[], long arraySize); // form 3
void sysSetVariableAsync(SysVarName, long value); // form 4
void sysSetVariableAsync(SysVarName, long values[], long arraySize); // form 5
void sysSetVariableAsync(SysVarName, int64 value); // form 6
void sysSetVariableAsync(SysVarName, char value[]); // form 7
```

## Description

Assigns the given value (data, value or values[]) to the system variable with identifier SysVarName. The bytes of data buffers are copied to struct, generic data and byte array system variables (form 1). The content of a character string is copied to String system variables (form 7). Floating point or integer numbers and arrays are assigned to the corresponding types of system variables (form 2 – 6).

The assignment is executed asynchronously. When measurement setup parallelization is activated, other branches in the measurement setup will see the new value earlier or later than the branch where the function is called.

In contrast to sysSetVariable* functions, sysSetVariableAsync do not prevent a measurement setup branch from being parallelized.

## Parameters

| Name | Description |
|---|---|
| SysVarName | System variable name.Must exist in the database. |
| data, value or values[] | New value for the system variable (form 1, 2) or buffer with new data (form 3, 4). |
| size | The number of bytes to be copied (form 1). |
| arraySize | The number of elements to be copied (form 3, 5). |

## Return Values

—

## Example

```c
byte dataBuf[64];
...

// Assign the value 0 to system variable Switch
sysSetVariableAsync(sysvar::Switch, 0);

// Assign the value 22.5 to system variable Temperature
sysSetVariableAsync (sysvar::Temperature, 22.5);

// Assign the value Master to system variable NodeName
sysSetVariableAsync (sysvar::NodeName, "Master");

// Copy 64 bytes of the data buffer into the system variable DiagData
sysSetVariableAsync (sysvar::DiagData, dataBuf, 64);

...
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | 13.0: form 6 | 14 | — |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | ✔ | N/A | — |
| CANoe Simulation Setup | N/A | — | — | — | N/A | — |
| CANoe System and Communication Setup | N/A | — | — | — | — | — |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | — |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | — |
| 32-Bit | — | — | — | N/A | — | — |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | — |
