# J1939ILOnCA

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILOnCA(long newAddress)
```

## Description

This callback function is called from the J1939 IL when a Command Address message is received.

The assignment of the new address can be suppressed.

## Parameters

| Name | Description |
|---|---|
| newAddress | 0 – 253: new address that ECU can accept 254: ECU has to go offline |

## Example

```c
long J1939ILOnCA(long address)
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
| Since Version | — | 5.2 | 13.0 | — | — | — |
| Restricted To | — | J1939 | J1939 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
