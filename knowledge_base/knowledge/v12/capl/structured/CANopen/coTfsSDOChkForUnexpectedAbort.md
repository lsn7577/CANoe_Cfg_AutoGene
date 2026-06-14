# coTfsSDOChkForUnexpectedAbort

> Category: `CANopen` | Type: `function`

## Syntax

```c
dword coTfsSDOChkForUnexpectedAbort( void );
```

## Description

This functions checks for unexpected SDO abort codes that are not in the list of accepted SDO abort codes. Therefore the function compares the list of received SDO abort codes with the list of accepted SDO abort codes.

The user has to reset both SDO abort code lists: the list of received SDO abort codes and the list of accepted SDO abort codes.

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
