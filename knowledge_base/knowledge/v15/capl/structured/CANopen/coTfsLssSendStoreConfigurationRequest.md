# coTfsLssSendStoreConfigurationRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendStoreConfigurationRequest( byte[] pErrorCode, byte[] pSpecificError );
```

## Description

The function sends a LSS Store Configuration request and waits for the response.

## Parameters

| Name | Description |
|---|---|
| pErrorCode | Error code. 0 - protocol successfully completed1 - store configuration not supported2 - storage media access error255 - implementation specific error occurred |
| pSpecificError | Manufacturer specific error (used if error code = 255). |

## Return Values

Error code

## Example

```c
byte pErrorCode[1];
byte pSpecificError[1];

/* send LSS store configuration request */

if (coTfsLssSendStoreConfigurationRequest( pErrorCode, pSpecificError) == 1) {
  /* sent LSS store configuration request and received response */
  /* received values can be found in pErrorCode[0], pSpecificError[0] */
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
