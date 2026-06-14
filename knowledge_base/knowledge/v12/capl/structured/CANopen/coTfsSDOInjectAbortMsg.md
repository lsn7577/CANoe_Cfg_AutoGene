# coTfsSDOInjectAbortMsg

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOInjectAbortMsg( dword canId, dword index, dword subIndex, dword abortCode, dword transmitCounter, dword replace );
```

## Description

This function inserts a SDO Abort Code message during the following cotfs command. Only one message is supported and the insertion is only possible for the directly following command. The inserted message is sent directly after the x.message, whereas x is defined with transmitCounter.

If less messages than expected are sent by the following command (transmitCounter number of sent messages), the insertion of the message is canceled.

## Return Values

Error code

## Example

```c
long retValFunc = kTestStepPassed; /* to store the return value of function */

long nodeId = 112;                              /* Node-Id of DUT */
dword msgCanId = 0;                             /* can id to be use */
dword msgDlc = 0;                               /* dlc to be use */
dword isRtr = 0;                                /* specifies if the message is a rtr frame */
dword transmitCounter = 0;                      /* indicate the position */
dword replace = 0;                              /* insert or replace */
dword abortCode = 0;                            /* abort code to be inserted */
dword index = 0x2001;                           /* object index */
dword subIndex = 0;                             /* object sub-index */
dword size = 0;                                 /* size of data in bytes */
byte inValueBuf[5] = {0x0, 0x0, 0x0, 0x0, 0x0}; /* data */
dword valueBufSize = 5;                         /* buffer size */
long retValFuncTemp = kTestStepPassed;          /* to store the return value of function */
byte resetFailControl= 0;                       /* flag to manage the failure control */
char msg[500];                                  /* message */

/* Tip:
  * For the used object [0x2001,0x0] is assumed:
  * - that it exits and it is writable
  * - that it can receive 5 bytes for a normal transfer
  *
  * The function cotfsSDOInjectAbortMsg inserts an abort message in the sequence
*/

retValFunc = kTestStepPassed;
msg[0] = '\0';
resetFailControl = 0;
retValFuncTemp = kTestStepPassed;

/* Set the node-ID of DUT */
strncat(msg,"Set node-ID\n", elCount(msg));
retValFunc = coTfsSetNodeId(nodeId);

/* prepare data for injection */
if (retValFunc == kTestStepPassed)
{
  strncat(msg,"cotfsSDOInjectAbortMsg - general error\n", elCount(msg));
  msgCanId = 0x600 + nodeId;
  abortCode = 0x08000000; /* General error */
  transmitCounter = 1;
  replace = 1;
  retValFunc = coTfsSDOInjectAbortMsg( msgCanId /*dword canId*/, index /*dword index*/, subIndex /*dword subIndex*/, abortCode /*dword abortCode*/, transmitCounter /*dword transmitCounter*/, replace /*dword replace*/ );
} /* if */

/* set failure control */
if (retValFunc == kTestStepPassed)
{
  strncat(msg,"coTfsSetFailControl - user\n", elCount(msg));
  retValFunc = coTfsSetFailControl(kHandleTestResultManually);
  resetFailControl = 1;
} /* if */

/* perform a download */
if (retValFunc == kTestStepPassed)
{
  strncat(msg,"coTfsSDODownload\n", elCount(msg));
  retValFuncTemp = coTfsSDODownload( index /*dword index*/, subIndex /*dword subIndex*/, size /*dword size*/, inValueBuf /*byte inValueBuf[]*/, valueBufSize /*dword valueBufSize*/ );

  /* re-assign the value */
  if (retValFuncTemp == kTestStepPassed)
  {
    strncat(msg,"coTfsSDODownload has to be failed !\n", elCount(msg));
    retValFunc = (!kTestStepPassed);
  } // if
} /* if */

/* reset failure control */
if (resetFailControl == 1)
{
  strncat(msg,"coTfsSetFailControl - normal behavior", elCount(msg));
  retValFuncTemp = coTfsSetFailControl(kHandleTestResultStandard);
  if (retValFuncTemp != kTestStepPassed)
  {
    retValFunc = (!kTestStepPassed);
  }
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
