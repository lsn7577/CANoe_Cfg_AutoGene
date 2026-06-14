# SecurityLocalGenerateSHA512

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalGenerateSHA512(byte data[], dword dataLength, byte sha512[], dword sha512Length)
```

## Description

Generates a SHA512 hash for the given data and using the given key.

## Parameters

| Name | Description |
|---|---|
| byte data[] | The data to encrypt. |
| dword dataLength | The length of the data to encrypt. |
| byte sha512[] [Out] | The generated SHA512 hash. |
| dword sha512Length [In/Out] | The length of the generated SHA512 hash (64 bytes). |

## Example

```c
byte data[3] = { 0x61, 0x62, 0x63 };
byte refOutput[64] ={
  0xdd, 0xaf, 0x35, 0xa1, 0x93, 0x61, 0x7a, 0xba
  , 0xcc, 0x41, 0x73, 0x49, 0xae, 0x20, 0x41, 0x31
  , 0x12, 0xe6, 0xfa, 0x4e, 0x89, 0xa9, 0x7e, 0xa2
  , 0x0a, 0x9e, 0xee, 0xe6, 0x4b, 0x55, 0xd3, 0x9a
  , 0x21, 0x92, 0x99, 0x2a, 0x27, 0x4f, 0xc1, 0xa8
  , 0x36, 0xba, 0x3c, 0x23, 0xa3, 0xfe, 0xeb, 0xbd
  , 0x45, 0x4d, 0x44, 0x23, 0x64, 0x3c, 0xe8, 0x0e
  , 0x2a, 0x9a, 0xc9, 0x4f, 0xa5, 0x4c, 0xa4, 0x9f
};

dword refOutputLength = 64;
byte output[64];
dword outputLength = 64;
dword result = 255;
dword counter = 0;
result = SecurityLocalGenerateSHA512(data, elCount(data), output, outputLength);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | 11.0 SP3 | — | — | — |
| Restricted To | — | CAN, CAN FD, FR, ETH | CAN, CAN FD, FR, ETH | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
