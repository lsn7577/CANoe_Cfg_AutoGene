# coTfsArrToW

> Category: `CANopen` | Type: `function`

## Syntax

```c
word coTfsArrToW( byte inByteArray[], dword arraysize );
```

## Description

The function converts the content of a byte array into a word value.

## Return Values

Converted value or 0 if parameters are invalid.

## Example

```c
/* converts a data from a byte array to a word */
Byte inDataArr[2] = {2,1};
Word outValue;

outValue = coTfsArrToW(inDataArr, 2);
```
