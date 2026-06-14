# coTfsSDOSetAbortControl

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOSetAbortControl( dword controlValue);
```

## Description

The function defines which values are allowed for successful test completion.

## Parameters

| Name | Description |
|---|---|
| controlValue | 1: correct response or accepted SDO abort code (see coTfsSDOAddAccAbortCode) is allowed for successful test completion, default 2: correct response or any SDO abort code is allowed 3: correct response is not allowed 4: correct response is not allowed but any SDO abort code |

## Return Values

Error code

## Example

```c
/* Accept correct answer or all SDO abort codes, which are in the list of accepted SDO abort codes to pass a test. */
const kSetAbortControlDefault = 1;

/* Accept correct answer or any SDO abort code to pass a test. */
const kSetAbortControlAllSDOAborts = 2;

/* Accept all SDO abort codes, which are in the list of accepted SDO abort codes to pass a test. The correct answer is not valid. */
const kSetAbortControlOnlySdoAbort = 3;

/* Accept any SDO abort codes to pass a test. The correct answer is not valid. */
const kSetAbortControlOnlyAnySdoAbort = 4;

/* Set internal handling of correct answers and SDO abort codes for level 2 SDO test functions.*/
if (coTfsSDOSetAbortControl(kSetAbortControlDefault) != 1)
{
  /* command failed */
} /* if */

/* now run any SDO level 2 function like coTfsSDOUpload(), ... */
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
