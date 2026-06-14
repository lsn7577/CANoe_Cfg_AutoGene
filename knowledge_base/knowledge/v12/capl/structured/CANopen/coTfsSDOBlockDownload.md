# coTfsSDOBlockDownload

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOBlockDownload( dword index, dword subIndex, dword size, dword useCrc, byte inValueBuf[], dword valueBufSize, dword outCrcUsed[] );
```

## Description

This function executes a complete SDO block download. This function can be used to exchange simple larger quantities of data with a CANopen® device insofar as it supports the block transfer. A fallback to segmented transfer is not supported.

The parameter useCrc reports if a CRC check was executed during transmission.

## Return Values

Error code

## Example

```c
byte pData[50];
dword outCrc[1];

// ... copy data to pData ...

if (coTfsSDOBlockDownload(0x2000, 0, 32, 1, pData, 50, outCrc) != 1) {
  TestStepFail("SDO block download test failed");
}
```
