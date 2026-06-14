# coTfsWToArr

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsWToArr( word wordValue, byte outByteArray[], dword arraysize );
```

## Description

The function converts a word value into a byte array.

## Return Values

Error code

## Example

```c
/* converts a word value to a byte array */
Word inValue = 2345;
Byte outDataArr[2];

if (coTfsWToArr(inValue, outDataArr, 2) != 1)
{
  /* conversion failed */
} /* if */
```
