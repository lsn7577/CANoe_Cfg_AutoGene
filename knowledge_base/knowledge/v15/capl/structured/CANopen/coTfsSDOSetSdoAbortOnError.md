# coTfsSDOSetSdoAbortOnError

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOSetSdoAbortOnError( dword setSdoAbort );
```

## Description

This function enables/disables sending a SDO abort code by the test module if a SDO access by SDO Level 2 functions or other test functions, that implicitly uses the SDO functionality, has failed. The setting is used until a new call of this function. For this the node-ID of the test module and the SDO abort code 0x8000 0000 (general error) is used.

## Parameters

| Name | Description |
|---|---|
| setSdoAbort | 0: no SDO abort message is sent in error cases (default) 1: a SDO abort message is sent in error cases |

## Return Values

Error code

## Example

```c
coTfsSDOSetSdoAbortOnError (1); /* if a SDO error is encountered, the SDO abort message will be sent from now */

coTfsSdoUpload(0x1000,0);

/* set default value – disable automatic sending of SDO abort messages by the test module */
coTfsSDOSetSdoAbortOnError (0);
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
