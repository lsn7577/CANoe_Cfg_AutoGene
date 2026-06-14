# memcpy

> Category: `StructByteAccess` | Type: `function`

## Syntax

```c
void memcpy(byte dest[], struct * source); // form 1
void memcpy(char dest[], struct * source); // form 2
void memcpy(byte dest[], long offset, struct * source); // form 3
void memcpy(char dest[], long offset, struct * source); // form 4
void memcpy(struct * dest, byte source[]); // form 5
void memcpy(struct * dest, char source[]); // form 6
void memcpy(struct * dest, byte source[], long offset); // form 7
void memcpy(struct * dest, char source[], long offset); // form 8
void memcpy(struct * dest, struct * source); // form 9
void memcpy(byte dest[], byte source[], dword length); // form 10
void memcpy(byte dest[], char source[], dword length); // form 11
void memcpy(char dest[], byte source[], dword length); // form 12
void memcpy(char dest[], char source[], dword length); // form 13
void memcpy(struct dest, char source[]); // form 14
void memcpy(struct dest, byte source[]); // form 15
void memcpy(char dest[], struct source); // form 16
void memcpy(byte dest[], struct source); // form 17
void memcpy(PDUPayload dest, PDUPayload source, dword length); // form 18
void memcpy(PDUPayload dest, byte source[], dword length); // form 19
void memcpy(byte source[], PDUPayload dest, dword length); // form 20
void memcpy(PDUPayload dest, struct * source); // form 21
void memcpy(struct * dest, PDUPayload source); // form 22
void memcpy(bytes dest, byte source[]); // form 23
void memcpy(bytes dest, char source[]); // form 24
void memcpy(bytes dest, byte source[], dword length); // form 25
void memcpy(bytes dest, char source[], dword length); // form 26
void memcpy(byte dest[], bytes source); // form 27
void memcpy(char dest[], bytes source); // form 28
```

## Description

Copies bytes from a source to a destination. In form 5, both structs must have the same type. In other forms with structs, the arrays must be large enough to contain the struct data. In form 17 and 18, the payload size and the struct size must be identical.

## Parameters

| Name | Description |
|---|---|
| source | (form 1, 2, 5): Struct whose bytes shall be copied. (form 14, 15, 17): Payload data of a PDU whose bytes shall be copied. (form 27, 28): vCDL "bytes" value that shall be copied. (other forms): Array whose bytes shall be copied. |
| dest | (form 3, 4, 5, 6, 7): Struct into which the bytes shall be copied. (form 14, 16, 18): Payload data of a PDU into which the bytes shall be copied. (form 23, 24, 25, 26): vCDL "bytes" value into which the bytes shall be copied. (other forms): Array into which the bytes shall be copied. |
| offset | (form 2, 4, 7): Offset in the array which marks the start of the data. |
| length | (form 8, 9, 10, 11, 14, 15, 16, 25, 26): number of bytes which shall be copied. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.0 SP3: form 1 7.2: form 7-13 9.0: form 14 10.0 SP3: form 15-18 15: form 23-28 | 7.0 SP3: form 1 7.2: form 7-13 9.0: form 14 10.0 SP3: form 15-18 15: form 23-28 | 13.0 15: form 23-28 | 13.0 15: form 23-28 | 14 15: form 23-28 | 1.0: form 1-13 2.1: form 14 2.2 SP2: form 15-18 15: form 23-28 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
