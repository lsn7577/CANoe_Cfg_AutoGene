# coTfsODAddEntry

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsODAddEntry( dword index, dword subIndex, dword accessType, dword entrySize, byte inMaskBuf[], dword maskBufSize, byte inValueBuf[], dword valueBufSize );
long coTfsODAddEntry( dword index, dword subIndex, dword accessType, dword entrySize, qword mask, qword inValue );
```

## Description

This function adds one object to the internal list of test objects. The test module manages an internal list for all object dictionary tests. Although certain object dictionary tests do not make use of all information provided, the usage of valid data is recommended.

Object entries with variable object length are supported too if the data length supplied equals 0. In this case value checks are not performed. The value mask is assumed to be open.

This function does not provide a stand-alone test. Instead it shall be used as a preparation for the test sequence functions coTfsODChk and coTfsODChkNotExist.

It may be possible, that the valid data range cannot be described using just one value. Therefore it is possible to add additional values using coTfsODAddOptEntryValue. coTfsODAddOptEntryValueRange allows the addition of complete value ranges. It is possible to combine both. Furthermore the valid range may overlap.

The compare mask flags all bits, which shall be compared.

## Parameters

| Name | Description |
|---|---|
| index | Checked object index. |
| subIndex | Checked object sub index. |
| accessType | 1: readWrite 2: readOnly 3: writeOnly 4: constant |
| entrySize | Data size of object in bytes. |
| inMaskBuf[] | Mask for data comparison, the size must be at least same as maskBufSize. 0: don't care 1: execute comparison |
| maskBufSize | Size of buffer. |
| inValueBuf[] | Data for comparison, the size must be at least same as size of valueBufSize. |
| valueBufSize | Size of buffer. |
| mask | Mask for data comparison. |
| inValue | Data for comparison. |

## Return Values

Error code

## Example

```c
long retValFunc = kTestStepPassed; /* to store the return value of function */
long nodeId = 112;                 /* Node-Id of DUT */

dword index = 0x1017;
dword subIndex = 0x0;
dword accessType = kAccessType_ReadWrite;
dword entrySize = 2; /* object size in bytes */
byte inMaskBuf[2] = {0xFF, 0xFF};
dword maskBufSize = 2;
byte inValueBuf[2] = {0x0, 0x0};
dword valueBufSize = 2;
char msg[100]; /* message */
retValFunc = kTestStepPassed;
msg[0] = '\0';

/* Set the node-ID of DUT */
strncpy(msg,"Set node-ID", elCount(msg));
retValFunc = coTfsSetNodeId(nodeId);

/* call test function : clear test object list */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsODClearAllEntries", elCount(msg));
  retValFunc = coTfsODClearAllEntries();
} /* if */

/* call test function : add entry to test object list */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsODAddEntry", elCount(msg));
  retValFunc = coTfsODAddEntry( index /*dword index*/, subIndex /*dword subIndex*/, accessType /*dword accessType*/, entrySize /*dword entrySize*/, inMaskBuf /*byte inMaskBuf[]*/, maskBufSize /*dword maskBufSize*/, inValueBuf /*byte inValueBuf[]*/, valueBufSize /*dword valueBufSize*/ );
} /* if */

/* call test function : check objects in test object list */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsODChk", elCount(msg));
  retValFunc = coTfsODChk();
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
