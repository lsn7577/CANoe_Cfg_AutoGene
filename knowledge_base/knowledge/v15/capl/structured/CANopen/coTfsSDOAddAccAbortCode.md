# coTfsSDOAddAccAbortCode

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOAddAccAbortCode( dword abortCode );
long coTfsSDOAddAccAbortCode( dword abortCode, dword definedByStandard);
```

## Description

The function adds an abort code to the internal list of accepted abort codes for testing devices. If the DUT (Device under test) responds with one of the abort codes in the list, the test is set to passed.

The functions must be called before executing SDO downloads or uploads.

## Parameters

| Name | Description |
|---|---|
| Note These reserved values are deprecated and replace by values of coTfsSDOSetAbortControl: 0x00000000: a correct response of the DUT is not accepted (see the following note) 0xFFFFFFFF: each abort code is accepted |  |
| Note If the SDO abort code is set to 0, the response behavior of all test functions (except the object dictionary tests) is modified. That means that e.g. NMT functions have to answer with SDO abort codes too. So a reset of the abort code list with coTfsSDOResetAccAbortList is necessary after using this function. |  |
| definedByStandard | 0: the abort code is interpreted as a user specific abort code and marked with "Warning" in the test report, default !=0: the abort code is interpreted as a standard abort code and marked with "Pass" in the test report |

## Return Values

Error code

## Example

```c
/* SDO abort code 0x06090000 will be accepted as an valid answer to pass a level 2 SDO function test,if coTfsSDOSetAbortControl is set to value 1 and 3.*/
if (coTfsSDOAddAccAbortCode(0x06090000) != 1)
{
  /* failed */
} /* if */
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
