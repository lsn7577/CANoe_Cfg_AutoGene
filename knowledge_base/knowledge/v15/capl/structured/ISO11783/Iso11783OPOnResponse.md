# Iso11783OPOnResponse

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783OPOnResponse( dword ecuHandle, pg VTtoECU response );
```

## Description

The function is called by the node layer, if a response from the Virtual Terminal is received. If a response is not received, the callback function Iso11783OPOnError is called.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU |
| response | Parameter group containing the answer of the Virtual Terminal |

## Return Values

—

## Example

```c
void Iso11783OPOnResponse( dword handle, pg VTtoECU response )
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
