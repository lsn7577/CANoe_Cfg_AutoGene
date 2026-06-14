# coTfsSDOUploadAndCompare

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOUploadAndCompare( dword index, dword subIndex, dword size, byte inValueBuf[], dword valueBufSize, byte inMaskBuf[], dword maskBufSize, dword useBitMask ); // form 1
```

## Description

This function executes a complete SDO upload. Depending on the number of data, this is either an expedited upload (up to 4 bytes) or a segmented transfer. Afterwards the received data is compared against the data supplied.

It is not possible to fetch the received data using coTfsGetSdoUploadData after this function was called.

(4) and (5) can be used for maximum 4 byte objects only.

## Return Values

error code or

## Example

```c
dword dataLength = 2;
byte compareMask[2];
byte receiveData[2];
receiveData[0] = 0x01;
receiveData[1] = 0x02;
compareMask[0] = 0x0F; /* compare only lower nibble of byte 0 */
compareMask[1] = 0xFF; /* compare complete byte 1 */

if (coTfsSDOUploadAndCompare( 0x1017, 0x2, dataLength, receiveData, 2, compareMask, 2, 1 ) != 1)
{
  write(" SDO upload failed or data mismatch");
}
```
