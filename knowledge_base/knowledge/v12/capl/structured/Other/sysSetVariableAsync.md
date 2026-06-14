# sysSetVariableAsync

> Category: `Other` | Type: `function`

## Syntax

```c
void sysSetVariableAsync(SysVarName, byte data[], long size); // form 1
```

## Description

Assigns the given value (data, value or values[]) to the system variable with identifier SysVarName. The bytes of data buffers are copied to struct, generic data and byte array system variables (form 1). The content of a character string is copied to String system variables (form 7). Floating point or integer numbers and arrays are assigned to the corresponding types of system variables (form 2 – 6).

The assignment is executed asynchronously. When measurement setup parallelization is activated, other branches in the measurement setup will see the new value earlier or later than the branch where the function is called.

In contrast to sysSetVariable* functions, sysSetVariableAsync do not prevent a measurement setup branch from being parallelized.

sysSetVariableAsync is useful to set system variables during the simulation and read their value using the System COM object after the simulation has been stopped. For this purpose, system variables have to be configured to be used for analysis only.

The sysSetVariableAsync function can also be used for specific elements of a system variable of type struct or generic array. For this, add the element to the name of the variable. If you directly give the element name to the function instead of using strings, precede the name by sysvarMember:: instead of sysvar::.

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

| Since Version |
|---|
