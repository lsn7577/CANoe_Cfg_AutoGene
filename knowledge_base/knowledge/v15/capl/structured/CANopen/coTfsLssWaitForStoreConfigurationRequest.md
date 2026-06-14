# coTfsLssWaitForStoreConfigurationRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForStoreConfigurationRequest( dword errorCode, dword specificError );
```

## Description

This function waits for the LSS store configuration request and sends the response.

## Parameters

| Name | Description |
|---|---|
| errorCode | Error code. 0 - protocol successfully completed1 - store configuration not supported2 - storage media access error255 - implementation specific error occurred |
| specificError | Manufacturer specific error (used if error code = 255). |

## Return Values

Error code

## Example

```c
/* waits for LSS store configuration request */
if (coTfsLssWaitForStoreConfigurationRequest( 0, 0) == 1) {
  /* received LSS store configuration request, sent response with error code and specific error = 0 */
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
