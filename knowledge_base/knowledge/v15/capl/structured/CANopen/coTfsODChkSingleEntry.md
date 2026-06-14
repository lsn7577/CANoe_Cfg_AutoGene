# coTfsODChkSingleEntry

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsODChkSingleEntry( dword index, dword subIndex, dword accessType, dword entrySize, byte inMaskBuf[], dword maskBufSize, byte inValueBuf[], dword valueBufSize );
```

## Description

The function checks a single object dictionary entry of existence and size via a SDO upload. Additionally the value is compared with the given value. The compare mask defines which data bits are compared and musts be identical. The test is only executed if the access type of the object is not writeOnly.

The test was successful if the values of a mandatory object are correct. On an optional object, the SDO abort codes (0x08000000, 0x06020000 and 0x06090011) are accepted also.

On a positive comparison and access type readWrite, the read value is written.

## Parameters

| Name | Description |
|---|---|
| index | Checked object index. |
| subIndex | Checked object sub index. |
| accessType | 1 - readWrite 2 - readOnly 3 - writeOnly 4 - constant |
| entrySize | Data size of object in bytes. |
| inMaskBuf[] | Mask for data comparison, the size must be at least same as maskBufSize. 0 - don't care 1 - execute comparison |
| maskBufSize | Size of buffer. |
| inValueBuf[] | Data for comparison, the size must be at least same as size of valueBufSize. |
| valueBufSize | Size of buffer. |

## Return Values

Error code

## Example

```c
long retValFunc = kTestStepPassed; /* to store the return value of function */
long nodeId = 112;                 /* Node-Id of DUT */

dword index = 0x1000; /* device type */
dword subIndex = 0x0; /* sub-index */
dword accessType = kAccessType_ReadOnly;
dword entrySize = 4;
byte inMaskBuf[4] = {0xFF, 0xFF, 0xFF, 0xFF};
dword maskBufSize = 4;
byte inValueBuf[4] = {0x0, 0x0, 0x0, 0x0};
dword valueBufSize = 4;
char msg[100]; /* message */
retValFunc = kTestStepPassed;
msg[0] = '\0';

/* Set the node-ID of DUT */
strncpy(msg,"Set node-ID", elCount(msg));
retValFunc = coTfsSetNodeId(nodeId);

/* call test function */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsODChkSingleEntry", elCount(msg));
  retValFunc = coTfsODChkSingleEntry( index /*dword index*/, subIndex /*dword subIndex*/, accessType /*dword accessType*/, entrySize /*dword entrySize*/, inMaskBuf /*byte inMaskBuf[]*/, maskBufSize /*dword maskBufSize*/, inValueBuf /*byte inValueBuf[]*/, valueBufSize /*dword valueBufSize*/ );
} /* if */

/* evaluation of returned value */
if (retValFunc != kTestStepPassed)
{
  /* outputs a failure message to the Write Window */
  write("%s failed", msg);
  /* Set testfunction or test case as failed; The message will be appeared in report if it is enabled */
  /* testStepFail( "CAPL text", "%s failed", msg); */
} /* if */
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
