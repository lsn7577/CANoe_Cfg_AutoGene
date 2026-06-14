# Iso11783OPConnectEnvVar

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPConnectEnvVar( dword ecuHandle, char envVarName[], dword objectId );
```

## Description

Connects an object (variable, value or string) from the object pool to an environment variable.

If an object is changed, the new value is put the environment variable. And vice versa, if the value of an environment variable is changed, the new value is also written to the connected object. Additionally a Change String or Change Numeric Value command is sent to the Virtual Terminal.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU. The handle must be created with Iso11783CreateECU. |
| envVarName | Name of the environment variable |
| objectID | Identifier of the object in the object pool |

## Return Values

0 or error code

## Example

```c
Iso11783OPConnectEnvVar( handle, "EnvSprayer_AppRate", 1040 );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
