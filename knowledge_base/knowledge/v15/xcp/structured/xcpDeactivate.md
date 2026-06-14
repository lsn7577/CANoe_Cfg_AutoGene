# xcpDeactivate

> Category: `XCP` | Type: `function`

## Syntax

```c
long xcpDeactivate (char namespace[], char variable[]); // form 1
long xcpDeactivate (sysvar sysvar); // form 2
```

## Description

Upload and DAQ measurement will be deactivated.

## Parameters

| Name | Description |
|---|---|
| namespace | Namespace of the corresponding system variable. |
| variable | Name of the corresponding system variable. |
| sysvar | Name of the fully qualified name of the system variable, including all name spaces, separated by "::".The name must be preceded by "sysVar::" |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.5 | 13.0 | — | — | 1.0 |
| Restricted To | — | XCP | XCP | — | — | XCP |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
