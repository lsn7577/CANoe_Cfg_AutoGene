# getValue

> Category: `Other` | Type: `function`

## Syntax

```c
int getValue(EnvVarName); // form 1
float getValue(EnvVarName); // form 2
long getValue(EnvVarName, char buffer[]); // form 3
long getValue(EnvVarName, byte buffer[]); // form 4
long getValue(EnvVarName, byte buffer[], long offset); // form 5
float getValue(char name[]); // form 6
long getValue(char name[], char buffer[]); // form 7
long getValue(char name[], byte buffer[]); // form 8
long getValue(char name[], byte buffer[], long offset); // form 9
```

## Description

Determines the value of the environment variable with identifier EnvVarName/name. The type of the return value is based on the type of environment variable (int for discrete (form 1), float for continuous environment variables (form 2 and 6)). For character string environment variables (form 3 and 7) and environment variables with data bytes (form 4, 5, 8 and 9) the active value is saved to a buffer which you identify in the function call.

## Parameters

| Name | Description |
|---|---|
| EnvVarName | Environment variable name.Must exist in the database. |
| buffer | Return buffer (form 3, 4 and 5) |
| offset | Offset of the first data byte copied (form 5) |

## Example

```c
int val;
float fval;
char cBuf[25];
byte bBuf[64];
long copiedBytes;
...
// Assign to val the value of the environment variable Switch
val = getValue(Switch);
// Assign to fval the value of the environment variable Temperature
val = getValue(Temperature);
// Read the value of environment variable NodeName
copiedBytes = getValue(NodeName, cBuf);
// Read the value of environment variable DiagData
copiedBytes = getValue(DiagData, bBuf);
// Read the value of environment variable DiagData starting at position 32
copiedBytes = getValue(DiagData, bBuf, 32);
...
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | All | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
