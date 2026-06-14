# coTfsSDOAddAccAbortCode

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOAddAccAbortCode( dword abortCode );
```

## Description

The function adds an abort code to the internal list of accepted abort codes for testing devices. If the DUT (Device under test) responds with one of the abort codes in the list, the test is set to passed.

The functions must be called before executing SDO downloads or uploads.

## Parameters

| Name | Description |
|---|---|
| Note These reserved values are deprecated and replace by values of coTfsSDOSetAbortControl: 0x00000000: a correct response of the DUT is not accepted (see the following note) 0xFFFFFFFF: each abort code is accepted |  |

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
