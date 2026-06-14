# Iso11783OPLoadVersion

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPLoadVersion( dword ecuHandle, char versionName[] );
```

## Description

The function loads an object pool, which is stored on the Virtual Terminal. A Load Version command is sent to the Virtual Terminal.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU (must be created with Iso11783CreateECU) |
| versionName | Designator of the version. For VT version smaller than 5 the name must be 7 characters long. For VT version 5 and higher a name with more than 7 characters is sent with the Load Extended Version command. |

## Return Values

0 or error code

## Example

```c
Iso11783OPLoadVersion( 
 handle, "POOL01A" );
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
