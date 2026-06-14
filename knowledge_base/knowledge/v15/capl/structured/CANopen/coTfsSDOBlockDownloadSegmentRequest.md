# coTfsSDOBlockDownloadSegmentRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOBlockDownloadSegmentRequest( dword cont, dword seqNumber, byte inValueBuf[], dword valueBufSize, dword isLastSegment );
```

## Description

This function sends a single segmented SDO block download message and waits for the corresponding response.

## Parameters

| Name | Description |
|---|---|
| cont | 0: more segments will follow 1: last segment |
| seqNumber | Sequence number |
| inValueBuf[] | Data field for transfer data |
| valueBufSize | Buffer size in byte of inValueBuf |
| isLastSegment | 0: more segments follow 1: last segment of transmission |

## Return Values

Error code

## Example

See example of coTfsSDOGetBlockSize

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
