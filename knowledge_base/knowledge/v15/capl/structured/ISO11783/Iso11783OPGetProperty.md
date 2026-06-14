# Iso11783OPGetProperty

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPGetProperty( dword ecuHandle, char propertyName[] );
```

## Description

Returns a property of the Object Pool API, e.g. the supported VT version.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU. The handle must be created with Iso11783CreateECU. |
| propertyName | Key of the information: "Version“ VT version support 2..4, Default 3 "DebugLevel“ Controls the output to the Write Window 0: No output 1: Only errors 2: Warnings and errors 3: Information, warnings and errors |

## Example

```c
LONG version;
version = Iso11783OPGetProperty( handle, "Version" );
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
