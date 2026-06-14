# coTfsLssSendSwitchStateModeGlobalRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendSwitchStateModeGlobalRequest( dword mode );
```

## Description

This function sends a LSS switch state global mode request.

## Parameters

| Name | Description |
|---|---|
| mode | 0 - switch to waiting mode1 - switch to configuration mode |

## Return Values

Error code

## Example

```c
/* send LSS switch state global protocol request -> switch to waiting state (mode = 0) */

if (coTfsLssSendSwitchStateModeGlobalRequest( 0 ) != 1) {
  /* message could not be sent */
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
