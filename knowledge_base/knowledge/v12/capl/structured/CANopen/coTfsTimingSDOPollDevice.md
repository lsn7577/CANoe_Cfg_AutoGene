# coTfsTimingSDOPollDevice

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsTimingSDOPollDevice( dword index, dword subIndex, dword retryNumber );
```

## Description

The functions monitors the average response times of a SDO access on a device.

Test flow

The functions executes a SDO Upload on the specified object for retryNumber times. The statistics of the selected node are reset at the beginning of the test. The received data are not compared, only the data size must be identical.

Test result

Minimum, maximum and average value of the SDO response time are added to the test protocol. The read values are not representative for all objects.

## Return Values

Error code

## Example

```c
coTfsTimingSDOPollDevice( 0x1000, 0x1, 50 ); // run timing test on index 0x1000
```
