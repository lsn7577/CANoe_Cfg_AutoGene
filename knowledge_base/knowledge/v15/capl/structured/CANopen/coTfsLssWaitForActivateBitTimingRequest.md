# coTfsLssWaitForActivateBitTimingRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForActivateBitTimingRequest( dword[] pSwitchDelay );
```

## Description

This function waits for LSS Activate Bit-Timings Parameters request.

## Parameters

| Name | Description |
|---|---|
| pSwitchDelay | Duration (in ms) of the two periods of time to wait until the bit timing parameters switch is done (first period) and before transmitting any CAN message with the new bit timing parameters after performing the switch (second period). |

## Return Values

Error code

## Example

```c
dword pSwitchDelay[1];

/* waits for LSS activate bit timing request */
if (coTfsLssWaitForActivateBitTimingRequest( pSwitchDelay) == 1) {
  /* received LSS activate bit timing request */
  /* received values can be found in pSwitchDelay[0] */
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
