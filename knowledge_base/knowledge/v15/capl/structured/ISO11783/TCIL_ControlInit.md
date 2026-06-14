# TCIL_ControlInit

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_ControlInit(); // form 1
long TCIL_ControlInit(byte deviceName[8]); // form 2
long TCIL_ControlInit(dbNode tc, byte deviceName[8] ); // form 3
```

## Description

This function can only be used in on preStart, to suppress the auto-start function of the IL.

If the device name is not specified, the node attributes with the device name must be defined (Exception: If NMT is not active, the device name is not needed).

## Parameters

| Name | Description |
|---|---|
| tc | TC simulation node to apply the function. |
| deviceName | ISO11783 64-Bit device name (optional) |

## Example

Example form 1

```c
on preStart
{
TCIL_ControlInit();
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3) | ✔ (form 3) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3) | ✔ (form 3) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
