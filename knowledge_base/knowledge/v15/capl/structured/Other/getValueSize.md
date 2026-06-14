# getValueSize

> Category: `Other` | Type: `function`

## Syntax

```c
int getValueSize(envvarHandle envEnvVarName); // form 1
int getValueSize(char envvarName[]); // form 2
```

## Description

Returns the size of the environment variable value in bytes.

## Parameters

| Name | Description |
|---|---|
| EnvVarName | Environment variable name.Must exist in the database. |

## Return Values

Size of the data in bytes.

## Example

```c
int vSize;
...
// Size of the data of an environment variable of type integer
vSize = getValueSize(switch);
// Buffersize of an environment variable of type string
// (with terminating Null character)
vSize = getValueSize(nodename);
// Size of the data byffer of an environment variable of type data
vSize = getValueSize(DiagData);
...
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | All | 13.0 | 13.0: form 1 | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
