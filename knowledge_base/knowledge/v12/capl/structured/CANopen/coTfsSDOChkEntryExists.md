# coTfsSDOChkEntryExists

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOChkEntryExists( dword index, dword subindex );
```

## Description

This function checks with a SDO upload if the object is readable.

## Return Values

Error code or one of the following values

## Example

```c
/* check if object [1000,0] is readable. This function is mainly a SDO upload function, but the test report output differs to make it more useful to check if an optional object exists */
if (coTfsSDOChkEntryExists(0x1000, 0) != 1)
{
  /* entry does not exist, 0x1000 is mandatory, so something serious is wrong here */
} /* if */
```
