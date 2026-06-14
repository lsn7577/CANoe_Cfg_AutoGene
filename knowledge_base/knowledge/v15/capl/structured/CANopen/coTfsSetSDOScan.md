# coTfsSetSDOScan

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSetSDOScan( byte outBufDetected[], dword outBufSize );
```

## Description

This functions performs a SDO upload of the mandatory object 0x1000 to detect if a CANopen® device is available. The available devices will be added to the test report. For each found node the value of outBufDetected[node-ID-1] is set to 1, else to 0. Thus the size of the buffer should match the number of available node-IDs of the device profile at a minimum.

## Parameters

| Name | Description |
|---|---|
| outBufDetected | Buffer for registering the found nodes. |
| outBufSize | Size of buffer. |

## Return Values

Error code

## Example

```c
dword outBufSize = 127;
byte outBufDetected[outBufSize];

if (coTfsSetSDOScan( outBufDetected, outBufSize ) == 1) {
  write ("SDO scan successfully performed");
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
