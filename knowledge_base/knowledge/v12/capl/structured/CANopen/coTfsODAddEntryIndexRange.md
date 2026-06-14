# coTfsODAddEntryIndexRange

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsODAddEntryIndexRange( dword minIndex, dword maxIndex, dword subIndex, dword accessType, dword entrySize, byte inMaskBuf[], dword maskBufSize, byte inValueBuf[], dword valueBufSize );
```

## Description

The function adds several object entries to the internal list. The elements only differ in the given object index. The default value can have a maximum size of 32 bit. The list is used by coTfsODChk and coTfsODChkNotExist.

## Return Values

Error code

## Example

```c
long retValFunc = kTestStepPassed; /* to store the return value of function */
long nodeId = 112;                 /* Node-Id of DUT */

dword minIndex = 0x2001;
dword maxIndex = 0x2002;
dword subIndex = 0x0;
dword accessType = kAccessType_ReadWrite;
dword entrySize = 5; /* object size in bytes */
byte inMaskBuf[5] = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF};
dword maskBufSize = 5;
byte inValueBuf[5] = {'H', 'a', 'l', 'l', 'o'};
dword valueBufSize = 5;
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
  strncpy(msg,"coTfsODAddEntryIndexRange", elCount(msg));
  retValFunc = coTfsODAddEntryIndexRange( minIndex /*dword minIndex*/, maxIndex /*dword maxIndex*/, subIndex /*dword subIndex*/, accessType /*dword accessType*/, entrySize /*dword entrySize*/, inMaskBuf /*byte inMaskBuf[]*/, maskBufSize /*dword maskBufSize*/, inValueBuf /*byte inValueBuf[]*/, valueBufSize /*dword valueBufSize*/ );
} /* if */

/* call test function : check objects in test object list */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsODRunUserDownloadUploadAndCompareTest", elCount(msg));
  retValFunc = coTfsODRunUserDownloadUploadAndCompareTest();
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
