# coTfsSDOChkForUnexpectedAbort

> Category: `CANopen` | Type: `function`

## Syntax

```c
dword coTfsSDOChkForUnexpectedAbort( void );
```

## Description

This functions checks for unexpected SDO abort codes that are not in the list of accepted SDO abort codes. Therefore the function compares the list of received SDO abort codes with the list of accepted SDO abort codes.

## Return Values

Error code

## Example

```c
/* clear list with received SDO abort codes first */
coTfsSDOResetAbortList();

/* no SDO abort code is accepted to pass this test, configured accepted SDO abort codes are treated like expected responses */
coTfsSDOResetAccAbortList();

/* Try to read a non-existing object. The DUT will answer with an SDO abort code */
coTfsSdoUpload(0x999,0);

if (coTfsSDOChkForUnexpectedAbort() != 1)
{
  /* no SDO abort code occured: object exists or device is not connected ? */
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
