# Iso11783AppAddrClaimed

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783AppAddrClaimed( long ecuHandle );
```

## Description

Indicates that Address Claiming was performed successfully, which means that the control device is permitted to communicate on the CAN bus.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | ECU handle |

## Return Values

—

## Example

```c
dword Iso11783AppAddrClaimed( LONG ecuHandle )
{
  /* user code */
  return 0;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | Iso11783 | Iso11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
