# A664GetFunctionalStatus

> Category: `ADFX` | Type: `function`

## Syntax

```c
BYTE A664GetFunctionalStatus (PDU aPDU)
```

## Description

This function returns the Functional Status (FS) of an AFDX-PDU (FDS) if the FDS-mode is used. In frameMode, use FS-signals instead.

## Parameters

| Name | Description |
|---|---|
| aPDU | The AFDX-PDU (FDS) of which the status is to be retrieved. |

## Example

```c
on PDU * {
{
  int fs = 0;
  fs = a664GetFunctionalStatus(this);
  writeEx(-3,1, "FS of received PDU %s: %d", this.name, fs);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 SP3 | 9.0 SP3 | — | — | — | — |
| Restricted To | AFDX | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
