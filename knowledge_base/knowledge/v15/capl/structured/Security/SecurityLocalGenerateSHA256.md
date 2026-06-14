# SecurityLocalGenerateSHA256

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalGenerateSHA256(byte data[], dword dataLength, byte sha256[], dword sha256Length)
```

## Description

Generates a SHA256 hash for the given data and using the given key.

## Parameters

| Name | Description |
|---|---|
| byte data[] | The data to encrypt. |
| dword dataLength | The length of the data to encrypt. |
| byte sha256[] [Out] | The generated SHA256 hash. |
| dword sha256Length [In/Out] | The length of the generated SHA256 hash. (32 bytes) |

## Example

```c
byte data[3] = { 0x61, 0x62, 0x63 };
byte refOutput[32] ={
0xba, 0x78, 0x16, 0xbf,
0x8f, 0x01, 0xcf, 0xea,
0x41, 0x41, 0x40, 0xde,
0x5d, 0xae, 0x22, 0x23,
0xb0, 0x03, 0x61, 0xa3,
0x96, 0x17, 0x7a, 0x9c,
0xb4, 0x10, 0xff, 0x61,
0xf2, 0x00, 0x15, 0xad
};

dword refOutputLength = 32;
byte output[32];
dword outputLength = 32;
dword result = 255;
dword counter = 0;
result = SecurityLocalGenerateSHA256(data, elCount(data), output, outputLength);
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
