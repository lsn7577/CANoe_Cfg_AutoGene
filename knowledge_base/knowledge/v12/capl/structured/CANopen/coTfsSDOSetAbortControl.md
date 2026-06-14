# coTfsSDOSetAbortControl

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOSetAbortControl( dword controlValue);
```

## Description

The function defines which values are allowed for successful test completion.

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
