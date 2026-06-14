# Iso11783OPOnIdentifyWorkingSet

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPOnIdentifyWorkingSet( dword handle );
```

## Description

The function is called by the ISO11783 node layer to determine if the node layer is responsible for sending the Working Set Master message during the object pool initialization (after the VT status message appears).

If this callback function is not implemented or it returns the value 1, the Working Set Master message is sent by the ISO11783 node layer. The transmitted number of Working Set members is 1. If the return value of the function is 0, the ISO11783 node layer doesn’t send the Working Set Master message. Instead, the CAPL application sends the Working Set Master message.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU |

## Example

```c
LONG Iso11783OPOnIdentifyWorkingSet( dword handle )
{
  return 1;
}
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
