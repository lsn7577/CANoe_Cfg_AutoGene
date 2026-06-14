# memcmp

> Category: `StructByteAccess` | Type: `function`

## Syntax

```c
int memcmp(struct s, byte buffer[]); // form 1
```

## Description

Compares the bytes of the parameters. In form 3, both structs must have the same type.

## Return Values

0 if the bytes are equal; a value different from 0 if they are unequal

## Example

```c
byte data[4];
struct WrapDword
{
   dword dw;
} dwordWrapper;

int i;
for (i = 0; i < elcount(data); ++i)
   data[i] = i;
dwordWrapper.dw = 0x03020100;
if (memcmp(dwordWrapper, data) == 0)
write("Data represents the number: Little Endian is used.");
```

## Availability

| Since Version |
|---|
