# setJ1587TP

> Category: `J1587` | Type: `function`

## Syntax

```c
void setJ1587TP( j1587Param param, dword mode );
```

## Description

Selects the setting for the transport protocol to use when sending a J1587 parameter via the output function.

## Parameters

| Name | Description |
|---|---|
| param | J1587 parameter for which the setting is used |
| 0 (default) | select the transport protocol by means of the receiver (selector J1587_ReceiverMID) MID 127: Multisection other MID: CMP/CDP |
| 1 | disable use of any transport protocol |
| 2 | use Multisection |
| 3 | use CMP/CDP |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.0 | 6.0 | 13.0 | — | — | — |
| Restricted To | J1587 | J1587 | J1587 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
