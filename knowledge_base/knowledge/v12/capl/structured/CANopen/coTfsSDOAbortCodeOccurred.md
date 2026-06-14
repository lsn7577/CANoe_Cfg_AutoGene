# coTfsSDOAbortCodeOccurred

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOAbortCodeOccurred( dword resetAbortList );
```

## Description

This function checks if a previously executed coTfsSDO… command can be finished with a received and accepted SDO abort code.

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
