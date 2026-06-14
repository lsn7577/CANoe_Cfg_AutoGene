# sysGetVariableArrayLength

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
dword sysGetVariableArrayLength(char namespace[], char variable[]); // form 1
dword sysGetVariableArrayLength(SysVarName); // form 2
```

## Description

Returns the length of the array of the system variable.

## Parameters

| Name | Description |
|---|---|
| namespace | Name of the name space. |
| variable | Name of the variable. |
| SysVarName | Name of the fully qualified name of the system variable, including all name spaces, separated by "::". The name must be preceded by "sysVar::". |

## Return Values

For system variables of type data, returns the current size (in bytes) of the value.
For system variables of type long or float array, returns the number of elements in the array.
For system variables of type string, returns the length of the string, excluding the terminating 0 character.
For system variables of type long or float, returns 1.

## Example

```c
// calculate the norm of a vector
dword length, i;
double element, sum, norm;
sum = 0.0;
length = sysGetVariableArrayLength(sysvar::MyVariables::MyVector);
for (i = 0; i < length; ++i) 
{
   element = @sysvar::MyVariables::MyVector[i];
   sum += element * element;
}
norm = sqrt(sum);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.0 SP4 | 7.0 SP4 | 13.0 | 13.0: form 2 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ (since version 7.2 SP3) | ✔ (since version 7.2 SP3) | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | • form 1 | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | • form 1 | N/A |
| 32-Bit | ✔ | — | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
