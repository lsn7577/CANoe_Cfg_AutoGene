# coTfsTPDOGetDataBySyncCyclic

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsTPDOGetDataBySyncCyclic( dword index, dword outLength[], byte outValueBuf[], dword valueBufSize );
```

## Description

This function tries to extract TPDO data using synchronous cyclic method of the test node.

Test sequence

Test result

The test was successful if all parts of the tests are executed successfully. If that's the case, the TPDO data are written in outLength[] and outValueBuf[]. Otherwise the data are set invalid.

Syntax special

The parameters outLength[] and outValueBuf[] can be omitted both.

## Parameters

| Name | Description |
|---|---|
| index | Index of TPDO. |
| outLength[] | Size of the TPDO in bytes. |
| outValueBuf[] | Data of the TPDO, the array size should be 8 bytes. |
| valueBufSize | Size of data buffer. |

## Return Values

Error code

## Example

```c
dword outLength[1];
byte outValueBuf[8];

if (coTfsTPDOGetDataBySyncCyclic( 0x1800, outLength, outValueBuf, 8 )!= 1) {
  write("could not retrieve data ");
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
