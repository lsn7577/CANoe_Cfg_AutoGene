# coTfsatoxL

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsatoxL( char inValueBuf[], dword valueBufSize );
```

## Description

The function converts a string in a long value.

The string contains either a decimal value, e.g. "1234" or a hexadecimal value, e.g. "0x4321". The prefix 0x is automatically detected and the function converts the string.

## Return Values

Converted string as long value.
