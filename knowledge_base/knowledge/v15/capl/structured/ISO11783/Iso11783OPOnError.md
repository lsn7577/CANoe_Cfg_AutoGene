# Iso11783OPOnError

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783OPOnError( dword ecuHandle, long error, dword vtFunction );
```

## Description

The function is called by the node layer, when the object pool detects an error.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU |
| error | Error code, see error codes 1102: Timeout during execution of a VT function, if response is not received 1103: Timeout of the status from VT, Object Pool API changes to state Wait for VT status |
| vtFunction | VT function which was executed when the error occurred |

## Return Values

—

## Example

```c
void Iso11783OPOnError( dword handle, LONG error, dword vtFunction )
{
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
