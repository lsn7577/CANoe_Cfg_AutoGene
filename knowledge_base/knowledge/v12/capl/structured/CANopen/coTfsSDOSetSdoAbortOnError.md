# coTfsSDOSetSdoAbortOnError

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOSetSdoAbortOnError( dword setSdoAbort );
```

## Description

This function enables/disables sending a SDO abort code by the test module if a SDO access by SDO Level 2 functions or other test functions, that implicitly uses the SDO functionality, has failed. The setting is used until a new call of this function. For this the node-ID of the test module and the SDO abort code 0x8000 0000 (general error) is used.

## Return Values

Error code

## Example

```c
coTfsSDOSetSdoAbortOnError (1); /* if a SDO error is encountered, the SDO abort message will be sent from now */

coTfsSdoUpload(0x1000,0);

/* set default value – disable automatic sending of SDO abort messages by the test module */
coTfsSDOSetSdoAbortOnError (0);
```
