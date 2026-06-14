# _DoIP_ConnectionClosedInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _DoIP_ConnectionClosedInd( long reason);
```

## Description

The TCP connection to the peer has been closed, i.e. another exchange of diagnostic messages will require a connection setup. This callback is also called in a vehicle simulation.

## Parameters

| Name | Description |
|---|---|
| reason | 0: The connection was closed by the node itself10054: The peer closed the connection Others: Reserved |

## Return Values

—

## Example

```c
void _DoIP_ConnectionClosedInd( long reason)
{
  write( "ConnectionClosedInd( %d)", reason);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP4 | — | — | — | 1.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
