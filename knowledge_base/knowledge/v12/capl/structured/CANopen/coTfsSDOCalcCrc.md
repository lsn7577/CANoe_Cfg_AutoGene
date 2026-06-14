# coTfsSDOCalcCrc

> Category: `CANopen` | Type: `function`

## Syntax

```c
dword coTfsSDOCalcCrc( byte inValueBuf[], dword valueBufSize );
```

## Description

This function calculates the CRC checksum for a block transfer (SDO block upload or SDO block download)- necessary for the calculation of the CRC across several data ranges).

## Return Values

CRC checksum

## Example

```c
byte inValueBuf[4] = {0x1, 0x2, 0x3, 0x4};
dword valueBufSize = 4;
dword crc = 0; /* to store the return value of function */

crc = coTfsSDOCalcCrc( inValueBuf, valueBufSize );

/* outputs a message to the 'write' window */
write( "coTfsSDOCalcCrc = %04X", crc);

/* The message will be appeared in report if it is enabled */
/* testStep( "CAPL text", "coTfsSDOCalcCrc = %04X", crc); */
```
