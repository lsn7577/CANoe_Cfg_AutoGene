# memcpy_off

> Category: `StructByteAccess` | Type: `function`

## Syntax

```c
void memcpy_off( struct type dest, dword destOffset, byte source[], dword sourceOffset, dword length); // form 1
void memcpy_off( struct type dest, dword destOffset, char source[], dword sourceOffset, dword length); // form 2
void memcpy_off( byte dest[], dword destOffset, struct type source, dword sourceOffset, dword length); // form 3
void memcpy_off( char dest[], dword destOffset, struct type source, dword sourceOffset, dword length); // form 4
void memcpy_off( byte dest[], dword destOffset, byte source[], dword sourceOffset, dword length); // form 5
void memcpy_off( char dest[], dword destOffset, byte source[], dword sourceOffset, dword length); // form 6
void memcpy_off( byte dest[], dword destOffset, char source[], dword sourceOffset, dword length); // form 7
void memcpy_off( char dest[], dword destOffset, char source[], dword sourceOffset, dword length); // form 8
```

## Description

Copies bytes from a source to destination, giving a destination start offset. The size of the destination must be at least destOffset + length.

## Parameters

| Name | Description |
|---|---|
| dest | (form 1, 2): Struct into which the bytes shall be copied.(other forms): Array into which the bytes shall be copied. |
| source | (form 3, 4): Struct from which the bytes shall be copied.(other forms): Array from which the bytes shall be copied. |
| destOffset | Start offset in the destination struct or array. |
| sourceOffset | Start offset int the source struct or array. |
| length | Number of bytes which shall be copied. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.2 | 7.2 | 13.0 | 13.0: form 2, 4, 8 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
