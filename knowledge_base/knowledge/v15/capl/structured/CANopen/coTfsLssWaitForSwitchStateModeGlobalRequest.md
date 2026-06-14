# coTfsLssWaitForSwitchStateModeGlobalRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForSwitchStateModeGlobalRequest( byte[] pMode );
```

## Description

This function waits for a LSS switch state global mode request.

## Parameters

| Name | Description |
|---|---|
| pMode | 0 - waiting mode1 - configuration mode |

## Return Values

Error code

## Example

```c
byte pMode[1];

/* waits for LSS switch state global request */
if (coTfsLssWaitForSwitchStateModeGlobalRequest() == 1) {
  /* received LSS switch state global request */
  /* value in pMode[0] */
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
