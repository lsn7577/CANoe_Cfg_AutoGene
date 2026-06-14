# coTfsLssWaitForFastScanRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForFastScanRequest( dword[] pId, byte[] pBitCheck, byte[] pSub, byte[] pNext );
```

## Description

This function waits for the Fast Scan message.

## Parameters

| Name | Description |
|---|---|
| pId | FastScan ID |
| pBitCheck | FastScan bitcheck value, used to define the used bitmask for LSS FastScan. |
| pSub | FastScan sub, defines which part of the LSS-ID is transmitted in idNumber. 0 - vendor-ID1 - product code2 - revision number3 - serial number |
| pNext | FastScan next, specifies the sub for the next request. |

## Return Values

Error code

## Example

```c
dword pId[1];
byte  pBitCheck[1];
byte  pSub[1];
byte  pNext[1];

/* waits for the fast scan request */
if (coTfsLssWaitForFastScanRequest( pId, pBitCheck, pSub, pNext ) == 1) {
  /* request received */
  /* received values can be found in pId, pBitCheck, pSub, pNext */
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
