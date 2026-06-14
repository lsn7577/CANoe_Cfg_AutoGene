# coTfsSDOBlockDownload

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOBlockDownload( dword index, dword subIndex, dword size, dword useCrc, byte inValueBuf[], dword valueBufSize, dword outCrcUsed[] );
```

## Description

This function executes a complete SDO block download. This function can be used to exchange simple larger quantities of data with a CANopen® device insofar as it supports the block transfer. A fallback to segmented transfer is not supported.

The parameter useCrc reports if a CRC check was executed during transmission.

## Parameters

| Name | Description |
|---|---|
| index | object index |
| subIndex | object sub index |
| size | number of bytes to be transmitted |
| useCrc | reports if CRC check was executed during transmission |
| inValueBuf[] | data field for transfer data |
| valueBufSize | buffer size in byte of inValueBuf |
| outCrcUsed[] | datafield, outCrcUsed[0] returns if a CRC check of the data was executed This check can only be done if both sided of the communication (test module and test node) support CRC checks. |

## Return Values

Error code

## Example

```c
byte pData[50];
dword outCrc[1];

// ... copy data to pData ...

if (coTfsSDOBlockDownload(0x2000, 0, 32, 1, pData, 50, outCrc) != 1) {
  TestStepFail("SDO block download test failed");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
