# Iso11783OPSetNumericValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPSetNumericValue( dword ecuHandle, dword objectID, long numericValue );
long Iso11783OPSetNumericValue( dword ecuHandle, dword objectID, long numericValue, long options );
```

## Description

The function sets the numerical value of an object. The object must exist in the object pool and must support a numerical value. If the Object Pool API is active, a Change Numeric Value command is sent to the Virtual Terminal. This can be suppress with Bit 0 in options.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU (must be created with Iso11783CreateECU) |
| objectID | Object ID of the object that has an updated value |
| numericValue | New value within the value range of the object |
| options | OptionsBit 0 = 1 Suppress Change Numeric Value command |

## Return Values

0 or error code

## Example

```c
Iso11783OPSetNumericValue( handle, 1000, 100 );
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
