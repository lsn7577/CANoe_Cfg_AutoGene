# putValueAsync

> Category: `Other` | Type: `function`

## Syntax

```c
void putValueAsync(EnvVarName, int val); // form 1
void putValueAsync(EnvVarName, float val); // form 2
void putValueAsync(EnvVarName, char val[]); // form 3
void putValueAsync(EnvVarName, byte val[], long vSize); // form 4
```

## Description

Assigns the value val to the environment variable with identifier EnvVarName. Integers are assigned to discrete environment variables (form 1), floating point numbers are assigned to continuous environment variables (form 2). The content of a character string is assigned to character string environment variables (form 3). For data byte environment variables (form 4) the bytes of the data buffer are copied into the environment variable.

The assignment is executed asynchronously. When measurement setup parallelization is activated, other branches in the measurement setup will see the new value earlier or later than the branch where the function is called.

In contrast to putValue, putValueAsync do not prevent a measurement setup branch from being parallelized.

## Parameters

| Name | Description |
|---|---|
| EnvVarName | Environment variable name.Must exist in the database. |
| vSize | New value of environment variable (form 1, 2) or buffer with new data (form 3, 4). |
| val | New value of environment variable (form 1, 2) or buffer with new data (form 3, 4). |

## Return Values

—

## Example

```c
byte dataBuf[64];
...

// Assign the value 0 to environment variable Switch
putValueAsync(Switch, 0);

// Assign the value 22.5 to environment variable Temperature
putValueAsync(Temperature, 22.5);

// Assign the value Master to environment variable NodeName
putValueAsync(NodeName, "Master");

// Copy 64 bytes of the data buffer into the environment variable DiagData
putValueAsync(DiagData, dataBuf, 64);

...
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | — |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | — | N/A | — |
| CANoe Simulation Setup | N/A | — | — | — | N/A | — |
| CANoe System and Communication Setup | N/A | — | — | — | — | — |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | — |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | — |
| 32-Bit | — | — | — | N/A | — | — |
| 64-Bit | — | ✔ | ✔ | — | — | — |
