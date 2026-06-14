# coTfsODAddOptEntryValueRange

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsODAddOptEntryValueRange( byte inMinValueBuf[], dword minValueBufSize, byte inMaxValueBuf[], dword maxValueBufSize );
```

## Description

The function expands the allowed value range of the last created object entry with the given value. The call of this function without coTfsODAddEntry is not allowed!

For the description of single values the function coTfsODAddOptEntryValue can be used.

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
byte inValueBuf[4] = {0x0, 0x0, 0x0, 0x0};
dword valueBufSize = 4;
byte inMinValueBuf[4] = {0x1, 0x2, 0x0, 0x0};  /* Generic pre-defined connection set for RPDO - Node 1 */
dword minValueBufSize = 4;
byte inMaxValueBuf[4] = {0x7F, 0x2, 0x0, 0x0}; /* Generic pre-defined connection set for RPDO - Node 2 */
dword maxValueBufSize = 2;
char msg[100]; /* message */

/*
* Purpose:
* Check if the COB-ID of the RPDO1 is equal to Zero or it is in the range between 0x201 and 0x27F
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
coTfsSetReportBehaviour(0xFFFFFFFF);

/* call test function : add entry to test object list */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsODAddEntry", elCount(msg));
  retValFunc = coTfsODAddEntry( index /*dword index*/, subIndex /*dword subIndex*/, accessType /*dword accessType*/, entrySize /*dword entrySize*/, inMaskBuf /*byte inMaskBuf[]*/, maskBufSize /*dword maskBufSize*/, inValueBuf /*byte inValueBuf[]*/, valueBufSize /*dword valueBufSize*/ );
} /* if */

/* call test function : add entry value range */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsODAddOptEntryValueRange", elCount(msg));
  retValFunc = coTfsODAddOptEntryValueRange( inMinValueBuf /*byte inMinValueBuf[]*/, minValueBufSize /*dword minValueBufSize*/, inMaxValueBuf /*byte inMaxValueBuf[]*/, maxValueBufSize /*dword maxValueBufSize*/ );
} /* if */

/* call test function : write objects in test object list */
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
