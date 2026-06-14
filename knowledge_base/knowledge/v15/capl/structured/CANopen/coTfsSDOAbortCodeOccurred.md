# coTfsSDOAbortCodeOccurred

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOAbortCodeOccurred( dword resetAbortList );
```

## Description

This function checks if a previously executed coTfsSDO… command can be finished with a received and accepted SDO abort code.

## Parameters

| Name | Description |
|---|---|
| resetAbortList | !=0: resets the list with received and accepted SDO abort codes (see coTfsSDOResetAbortList) |

## Return Values

Error code

## Example

```c
/* clear list with received SDO abort codes first */
coTfsSDOResetAbortList();

/* Try to read a non-existing object. The DUT will answer with an SDO abort code */
coTfsSdoUpload(0x999,0);

/* perform other SDO accesses ... */
/* did any SDO abort code occur ? */
if (coTfsSDOAbortCodeOccurred(1) != 1)
{
  /*
   * no SDO abort code occurred
   * object exists or device is not connected ?
  */
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
