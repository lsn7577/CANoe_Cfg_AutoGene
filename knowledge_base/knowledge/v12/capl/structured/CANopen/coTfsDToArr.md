# coTfsDToArr

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsDToArr( dword dwordValue, byte outByteArray[], dword arraysize );
```

## Description

The function converts a dword value into a byte array.

## Return Values

Error code

## Example

```c
/* converts a dword value to a byte array */
Dword inValue = 234567;
Byte outDataArr[4];

if (coTfsDToArr(inValue, outDataArr, 4) != 1)
{
  /* conversion failed */
} /* if */
```
