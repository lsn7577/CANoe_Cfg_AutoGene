# memcpy

> Category: `StructByteAccess` | Type: `function`

## Syntax

```c
void memcpy(byte dest[], struct source); // form 1
```

## Description

Copies bytes from a source to a destination. In form 5, both structs must have the same type. In other forms with structs, the arrays must be large enough to contain the struct data. In form 17 and 18, the payload size and the struct size must be identical.

## Return Values

—

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
memcpy(dwordWrapper, data);
write("Bytes as dword: %0#10lx", dwordWrapper.dw);
dwordWrapper.dw = 0x12345678;
memcpy(data, dwordWrapper);
write("dword as bytes: %#lx %#lx %#lx %#lx", data[0], data[1], data[2], data[3]);
```

## Availability

| Since Version |
|---|
