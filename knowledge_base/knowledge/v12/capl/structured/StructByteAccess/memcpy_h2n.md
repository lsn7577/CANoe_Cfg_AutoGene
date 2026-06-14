# memcpy_h2n

> Category: `StructByteAccess` | Type: `function`

## Syntax

```c
void memcpy_h2n(byte dest[], struct source); // form 1
```

## Description

Copies the bytes from the struct into the array, and translates the byte order of the elements from little-endian to big-endian (h2n stands for "host to network").

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
memcpy_n2h(dwordWrapper, data);
write("Bytes as dword: %0#10lx", dwordWrapper.dw);
dwordWrapper.dw = 0x12345678;
memcpy_h2n(data, dwordWrapper);
write("dword as bytes: %#lx %#lx %#lx %#lx", data[0], data[1], data[2], data[3]);
```

## Availability

| Since Version |
|---|
