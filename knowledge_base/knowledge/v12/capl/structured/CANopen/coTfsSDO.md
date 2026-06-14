# coTfsSDO

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDO( dword index, dword subIndex );
```

## Description

This function executes the following transfers:

In each case, first a value is written with a download and this value is read back with an upload and checked. The test is destructive, the object in the DUT Device Under Test is overwritten. The object's data is overwritten during the test and not restored. The block transfers are transmitted with a CRC checksum if the CANopen® device supports these.

The test counts as passed if all 6 data transmissions were completed successfully.

## Return Values

Error code

## Example

```c
if ( coTfsSDO (0x2000, 0x0) != 1) {
  write("SDO test failed");
}
```
