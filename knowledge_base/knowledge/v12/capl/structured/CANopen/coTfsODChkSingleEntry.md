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
