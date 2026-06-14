# memcpy_h2n

> Category: `StructByteAccess` | Type: `function`

## Syntax

```c
void memcpy_h2n(byte dest[], struct source); // form 1
void memcpy_h2n(byte dest[], int offset, struct source); // form 2
```

## Description

Copies the bytes from the struct into the array, and translates the byte order of the elements from little-endian to big-endian (h2n stands for "host to network").

## Parameters

| Name | Description |
|---|---|
| source | Struct whose bytes shall be copied |
| dest | Array into which the bytes shall be copied |
| offset (form 2) | Offset into the array |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.0 SP3 | 7.0 SP3 | 13.0 | 13.0 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
