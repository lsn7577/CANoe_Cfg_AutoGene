# coTfsODAddOptEntryValue

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsODAddOptEntryValue( byte inValueBuf[], dword valueBufSize );
```

## Description

The function expands the allowed value range of the last created object entry with the given value. The call of this function without coTfsODAddEntry is not allowed!

For the description of complete value ranges the function coTfsODAddOptEntryValueRange can be used.

## Return Values

Error code

## Example

```c
long retValFunc = kTestStepPassed; /* to store the return value of function */
long nodeId = 112;                 /* Node-Id of DUT */

dword index = 0x1400;
dword subIndex = 0x1;
dword accessType = kAccessType_ReadWrite;
dword entrySize = 4; /* object size in bytes */
byte inMaskBuf[4] = {0xFF, 0xFF, 0xFF, 0x1F}; /* check only the COB-ID value */
dword maskBufSize = 4;
byte inValueBuf[4] = {0x01, 0x02, 0x00, 0x80};
dword valueBufSize = 4;
char msg[100]; /* message */

/*
* Purpose:
* - Check it if the COB-ID of the RPDO1 is equal to 0x201, 0x270 or 0x272
* - Download the given values (0x201, 0x270 or 0x272) as COB-ID of the RPDO1
*/

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

/* call test function : add entry value */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsODAddOptEntryValue", elCount(msg));
  inValueBuf[0] = 0x70; /* 0x00000270*/
  inValueBuf[1] = 0x2;
  inValueBuf[2] = 0x0;
  inValueBuf[3] = 0x80;
  retValFunc = coTfsODAddOptEntryValue( inValueBuf /*byte inValueBuf[]*/, valueBufSize /*dword valueBufSize*/ );
} /* if */

/* call test function : add entry value */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsODAddOptEntryValue", elCount(msg));
  inValueBuf[0] = 0x72; /* 0x00000272*/
  inValueBuf[1] = 0x2;
  inValueBuf[2] = 0x0;
  inValueBuf[3] = 0x80;
  retValFunc = coTfsODAddOptEntryValue( inValueBuf /*byte inValueBuf[]*/, valueBufSize /*dword valueBufSize*/ );
} /* if */

/* call test function : write objects in test object list */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsODChk", elCount(msg));
  retValFunc = coTfsODChk();
} /* if */

/* call test function : write objects in test object list */
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
