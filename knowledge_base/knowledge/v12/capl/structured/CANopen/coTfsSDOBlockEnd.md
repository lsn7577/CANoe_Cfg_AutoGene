# coTfsSDOBlockEnd

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOBlockEnd( dword ccs, dword cs, dword notUsed, dword crc ); // form 1
```

## Description

This function sends a SDO block end response/request message (depending on a SDO block upload and SDO block download) and awaits the corresponding response.

(2) The parameter crcSetting is used for SDO block upload only.

## Return Values

Error code

## Example

```c
see example of coTfsSDOBlockInit
```
