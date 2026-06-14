# coTfsSetSDOScan

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSetSDOScan( byte outBufDetected[], dword outBufSize );
```

## Description

This functions performs a SDO upload of the mandatory object 0x1000 to detect if a CANopen® device is available. The available devices will be added to the test report. For each found node the value of outBufDetected[node-ID-1] is set to 1, else to 0. Thus the size of the buffer should match the number of available node-IDs of the device profile at a minimum.

## Return Values

Error code

## Example

```c
dword outBufSize = 127;
byte outBufDetected[outBufSize];

if (coTfsSetSDOScan( outBufDetected, outBufSize ) == 1) {
  write ("SDO scan successfully performed");
}
```
