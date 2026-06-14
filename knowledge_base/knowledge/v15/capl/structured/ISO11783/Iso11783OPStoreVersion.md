# Iso11783OPStoreVersion

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPStoreVersion( dword ecuHandle, char versionName[] );
```

## Description

The function stores the current object pool on the Virtual Terminal. A Store Version command is sent to the Virtual Terminal.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU (must be created with Iso11783CreateECU) |
| versionName | Name which is used to store the object pool. For VT version smaller than 5 the name must be 7 characters long. For VT version 5 and higher a name with more than 7 characters is sent with the Store Extended Version command. |

## Return Values

0 or error code

## Example

```c
Iso11783OPStoreVersion( 
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
