# Iso11783PDDOnDefaultLogRequest

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783PDDOnDefaultLogRequest( dword ecuHandle );
```

## Description

This function can be implemented in the CAPL program. The function is called up by the node layer if default logging is requested by the Task Controller. Default logging can then be started with the CAPL function Iso11783PDDSetLogTrigger.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU |

## Return Values

—

## Example

```c
void Iso11783PDDOnDefaultLogRequest( dword ecuHandle )
{
  Iso11783PDDSetLogTrigger ( ecuHandle, 4, 0x0100, 0, 1000 );
  Iso11783PDDSetLogTrigger ( ecuHandle, 4, 0x0101, 0, 1000 );
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
