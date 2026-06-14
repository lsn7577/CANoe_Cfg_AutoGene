# Iso11783OPSetStringValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPSetStringValue( dword ecuHandle, dword objectID, char stringValue[] );
long Iso11783OPSetStringValue( dword ecuHandle, dword objectID, char stringValue[], dword options );
```

## Description

The functions set the string value of an object in the object pool. The object must exist in the object pool and must support a string value. If the Object Pool API is active, a Change String Value command is sent to the Virtual Terminal. This can be suppressed with Bit 0 in options.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU (must be created with Iso11783CreateECU) |
| objectID | Object ID of the object that has an updated value |
| stringValue | Buffer containing new string value |
| options | OptionsBit 0 = 1 Suppress Change String Value command |

## Example

```c
Iso11783OPSetStringValue( handle, 1000, “Hello World” );
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
