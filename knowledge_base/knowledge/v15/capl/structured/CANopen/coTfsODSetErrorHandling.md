# coTfsODSetErrorHandling

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsODSetErrorHandling( dword enable );
```

## Description

The function controls the behavior of the test module while executing coTfsODChk and coTfsODChkNotExist. It can called before the two test sequences and define the behavior in an error case. It can be defined if the tests should stop in an error occurrence to execute the next command (breakOnError=1) or if the error should be ignored (breakOnError=0).

## Parameters

| Name | Description |
|---|---|
| enable | 0: test goes on after an error, all objects of the internal list are checked in the test 1: test is stopped |

## Return Values

Error code

## Example

```c
long retValFunc = kTestStepPassed; /* to store the return value of function */
long nodeId = 112;                 /* Node-Id of DUT */

dword index = 0x1400;
dword subIndex = 0x0;
dword accessType = kAccessType_ReadWrite;
dword entrySize = 2; /* object size in bytes */
byte inMaskBuf[4] = {0xFF, 0xFF, 0xFF, 0xFF};
dword maskBufSize = 4;
byte inValueBuf[4] = {0x00, 0x00, 0x00, 0x00};
dword valueBufSize = 4;
dword erroHandling = 0;
long retValFuncTemp = kTestStepPassed; /* to store the return value of function */
byte resetFailControl = 0;             /* flag to manage the failure control */
byte resetErrorHandling = 0;           /* flag to manage the failure control */
char msg[100];                         /* message */

/*
  * Purpose:
  * Check the existence ob sub-indexes 0, 1, 4 and 5 of RPDO1 communication parameter.
  * The execution of coTfsODChk is aborted(coTfsODSetErrorHandling), if a failure has 
  * been detected (sub-index 04 is reserved. It shall not be implemented).
*/

retValFunc = kTestStepPassed;
msg[0] = '\0';
resetFailControl = 0;
resetErrorHandling = 0;
retValFuncTemp = kTestStepPassed;

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
  strncpy(msg,"coTfsODAddEntry - Highest sub-index supported", elCount(msg));
  index = 0x1400;
  subIndex = 0x0;
  accessType = kAccessType_ReadOnly;
  entrySize = 1; /* object size in bytes */
  inMaskBuf[0] = 0x0;
  inMaskBuf[1] = 0x0;
  inMaskBuf[2] = 0x0;
  inMaskBuf[3] = 0x0;
  maskBufSize = 1;
  inValueBuf[0] = 0x0;
  inValueBuf[1] = 0x0;
  inValueBuf[2] = 0x0;
  inValueBuf[3] = 0x0;
  valueBufSize = 1;
  retValFunc = coTfsODAddEntry( index /*dword index*/, subIndex /*dword subIndex*/, accessType /*dword accessType*/, entrySize /*dword entrySize*/, inMaskBuf /*byte inMaskBuf[]*/, maskBufSize /*dword maskBufSize*/, inValueBuf /*byte inValueBuf[]*/, valueBufSize /*dword valueBufSize*/ );
} /* if */

/* call test function : add entry to test object list */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsODAddEntry - COB-ID", elCount(msg));
  index = 0x1400;
  subIndex = 0x1;
  accessType = kAccessType_ReadWrite;
  entrySize = 4; /* object size in bytes */
  inMaskBuf[0] = 0x0;
  inMaskBuf[1] = 0x0;
  inMaskBuf[2] = 0x0;
  inMaskBuf[3] = 0x0;
  maskBufSize = 4;
  inValueBuf[0] = 0x0;
  inValueBuf[1] = 0x0;
  inValueBuf[2] = 0x0;
  inValueBuf[3] = 0x0;
  valueBufSize = 4;
  retValFunc = coTfsODAddEntry( index /*dword index*/, subIndex /*dword subIndex*/, accessType /*dword accessType*/, entrySize /*dword entrySize*/, inMaskBuf /*byte inMaskBuf[]*/, maskBufSize /*dword maskBufSize*/, inValueBuf /*byte inValueBuf[]*/, valueBufSize /*dword valueBufSize*/ );
} /* if */

/* call test function : add entry to test object list */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsODAddEntry - reserved", elCount(msg));
  index = 0x1400;
  subIndex = 0x4;
  accessType = kAccessType_ReadOnly;
  entrySize = 1; /* object size in bytes */
  inMaskBuf[0] = 0x0;
  inMaskBuf[1] = 0x0;
  inMaskBuf[2] = 0x0;
  inMaskBuf[3] = 0x0;
  maskBufSize = 1;
  inValueBuf[0] = 0x0;
  inValueBuf[1] = 0x0;
  inValueBuf[2] = 0x0;
  inValueBuf[3] = 0x0;
  valueBufSize = 1;
  retValFunc = coTfsODAddEntry( index /*dword index*/, subIndex /*dword subIndex*/, accessType /*dword accessType*/, entrySize /*dword entrySize*/, inMaskBuf /*byte inMaskBuf[]*/, maskBufSize /*dword maskBufSize*/, inValueBuf /*byte inValueBuf[]*/, valueBufSize /*dword valueBufSize*/ );
} /* if */

/* call test function : add entry to test object list */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsODAddEntry - Event timer", elCount(msg));
  index = 0x1400;subIndex = 0x5;
  accessType = kAccessType_ReadWrite;
  entrySize = 2; /* object size in bytes */
  inMaskBuf[0] = 0x0;
  inMaskBuf[1] = 0x0;
  inMaskBuf[2] = 0x0;
  inMaskBuf[3] = 0x0;
  maskBufSize = 4;
  inValueBuf[0] = 0x0;
  inValueBuf[1] = 0x0;
  inValueBuf[2] = 0x0;
  inValueBuf[3] = 0x0;
  valueBufSize = 4;
  retValFunc = coTfsODAddEntry( index /*dword index*/, subIndex /*dword subIndex*/, accessType /*dword accessType*/, entrySize /*dword entrySize*/, inMaskBuf /*byte inMaskBuf[]*/, maskBufSize /*dword maskBufSize*/, inValueBuf /*byte inValueBuf[]*/, valueBufSize /*dword valueBufSize*/ );
} /* if */

/* set failure control */
if (retValFunc == kTestStepPassed)
{
  strncat(msg,"coTfsSetFailControl - user\n", elCount(msg));
  retValFunc = coTfsSetFailControl(kHandleTestResultManually);
  resetFailControl = 1;
} /* if */

/* call test function : break execution on failure in test object list */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsODSetErrorHandling", elCount(msg));
  erroHandling = kErrorHandling_StopOnFirstFailedTest; //stop on first failed test
  retValFunc = coTfsODSetErrorHandling( errorHandling /*dword errorHandling*/ );
  resetErrorHandling = 1;
} /* if */

/* call test function : check objects in test object list */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsODChk", elCount(msg));
  retValFuncTemp = coTfsODChk();
  /* re-assign the value */
  if (retValFuncTemp == kTestStepPassed)
  {
    strncat(msg,"coTfsODChk has to be failed !\n", elCount(msg));
    retValFunc = (!kTestStepPassed);
  } // if
} /* if */

if (resetErrorHandling == 1)
{
  strncat(msg,"coTfsODSetErrorHandling - run all test", elCount(msg));
  erroHandling = kErrorHandling_RunAllTests; //run all tests
  retValFuncTemp = coTfsODSetErrorHandling(errorHandling /*dword errorHandling*/);
  if (retValFuncTemp != kTestStepPassed)
  {
    retValFunc = (!kTestStepPassed);
  } /* if */
} /* if */

/* reset failure control */
if (resetFailControl == 1)
{
  strncat(msg,"coTfsSetFailControl - normal behavior", elCount(msg));
  retValFuncTemp = coTfsSetFailControl(kHandleTestResultStandard);
  if (retValFuncTemp != kTestStepPassed)
  {
    retValFunc = (!kTestStepPassed);
  } /* if */
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
