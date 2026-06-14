# memcmp

> Category: `StructByteAccess` | Type: `function`

## Syntax

```c
int memcmp(struct * dest, byte source[]); // form 1
int memcmp(byte dest[], struct * source); // form 2
int memcmp(struct * dest, struct * source); // form 3
int memcmp(byte dest[], byte source[], dword size); // form 4
```

## Description

Compares the bytes of the parameters. In form 3, both structs must have the same type.

## Parameters

| Name | Description |
|---|---|
| dest | A struct |
| source | Another struct |
| size | Size of the arrays (number of bytes to compare). |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.0 SP3: form 1-3 9.0 SP4: form 4 | 7.0 SP3: form 1-3 9.0 SP4: form 4 | 13.0 | 13.0 | 14 | 1.0: form 1-3 2.1 SP4: form 4 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
