# coTfsODChkNotExist

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsODChkNotExist( void );
```

## Description

This function executes an user defined object dictionary test on hidden objects.

Test preparation

The objects which are to test should be added to the internal list of the test objects with the following functions:

With the function coTfsODSetErrorHandling the behavior in an error case can be defined.

Test flow

The function checks every object dictionary entry of existence and size. Additionally the value is compared with the given value. The compare mask defines which data bits are compared and musts be identical.

The complete test is only executed if the access type of the object is not writeOnly.

On a positive comparison and access type readWrite, the read value is written also.

Test result

The test node must answer with a SDO abort code (0x08000000, 0x06020000 or 0x06090011) at all objects.

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

/*
* Purpose:
* Check the non-existing of objects [0x1017,0x55] and [0x1017,0xFF]
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
  subIndex = 0x55;
  retValFunc = coTfsODAddEntry( index /*dword index*/, subIndex /*dword subIndex*/, accessType /*dword accessType*/, entrySize /*dword entrySize*/, inMaskBuf /*byte inMaskBuf[]*/, maskBufSize /*dword maskBufSize*/, inValueBuf /*byte inValueBuf[]*/, valueBufSize /*dword valueBufSize*/ );
} /* if */

/* call test function : add entry to test object list */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsODAddEntry", elCount(msg));
  subIndex = 0xFF;
  retValFunc = coTfsODAddEntry( index /*dword index*/, subIndex /*dword subIndex*/, accessType /*dword accessType*/, entrySize /*dword entrySize*/, inMaskBuf /*byte inMaskBuf[]*/, maskBufSize /*dword maskBufSize*/, inValueBuf /*byte inValueBuf[]*/, valueBufSize /*dword valueBufSize*/ );
} /* if */

/* call test function : check objects in test object list */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsODChkNotExist", elCount(msg));
  retValFunc = coTfsODChkNotExist();
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
