# coTfsLssWaitForConfigureNodeIdRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForConfigureNodeIdRequest( byte[] pNID );
```

## Description

The function waits for the configure LSS node id request.

## Parameters

| Name | Description |
|---|---|
| pNID | Node-ID of the device, value range 1..127 and 255. |

## Return Values

Error code

## Example

```c
dword pNID[1];

/* waits for LSS configure node ID request */
if (coTfsLssWaitForConfigureNodeIdRequest( pNID) == 1) {
  /* received LSS configure node ID request */
  /* received values can be found in pNID[0] */
}
else {
  /* no request received */
  return;
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
