# FSIL_OnCA

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_OnCA(long newAddress);
```

## Description

Is called from the FS IL when a Command Address message is received.

The return value defines the node reaction to the Command Address message (the assignment of the new address can be suppressed).

## Parameters

| Name | Description |
|---|---|
| newAddress | 0..253: new address that ECU can accept 254: ECU has to go offline |

## Example

```c
long FSIL_OnCA(long address)
{
  if(address == 2)
    return 0; //don’t accept the address ‘2’
  else
    return 1;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
