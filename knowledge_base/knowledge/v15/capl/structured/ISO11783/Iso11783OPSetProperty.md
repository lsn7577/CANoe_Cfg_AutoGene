# Iso11783OPSetProperty

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPSetProperty( dword ecuHandle, char propertyName[], long newValue );
```

## Description

The function sets a property of the Object Pool API, i.e. the supported Virtual Terminal version.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU. The handle must be created with Iso11783CreateECU. |
| Version | Supported version of the ISO11783 Virtual Terminal specification.Supported values: 2, 3 (default), 4 and 5If used, the version value obtained from the database (node attribute ISO11783OPVersion) is overwritten. |
| DebugLevel | Controls the output to the Write Window. Supported values: 0: No output 1: Only errors 2: Warnings and errors 3: Information, warnings and errors |
| SendPreferredAssignmentEvenIfEmpty | Enforces sending of the Preferred Assigning message to the Virtual Terminal, even if no of auxiliary function has a preferred assigned auxiliary input, i.e. the corresponding INI file (i.g. Sprayer.ini) contains following lines: [AuxAssignment]AuxAssignmentCount=0 Supported values: 0: Preferred Assigning message is sent to the Virtual Terminal if at least one preferred assignment exists 1: Preferred Assigning message is sent to the Virtual Terminal even if no preferred assignment exists |
| newValue | New value for the parameter |

## Example

```c
Iso11783OPSetProperty( handle, "Version", 3 );
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
