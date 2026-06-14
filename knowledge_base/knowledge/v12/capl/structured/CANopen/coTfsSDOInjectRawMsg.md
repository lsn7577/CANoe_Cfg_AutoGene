# coTfsSDOInjectRawMsg

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOInjectRawMsg( dword canId, dword dlc, byte buf[], dword bufSize, dword isRtr, dword transmitCounter, dword replace );
```

## Description

This function inserts any CAN message during the following cotfs command. Only one message is supported and the insertion is only possible for the directly following command. The inserted message is sent directly after the x.message, whereas x is defined with transmitCounter.

If less messages than expected are sent by the following command (transmitCounter > number of sent messages), the insertion of the message is canceled.

## Return Values

Error code

## Example

```c
long retValFunc = kTestStepPassed; /* to store the return value of function */

long nodeId = 112;                              /* Node-Id of DUT */
dword msgCanId = 0;                             /* can id to be use */
dword msgDlc = 0;                               /* dlc to be use */
byte buf[8];                                    /* data to be transmitted */
dword bufSize = 8;                              /* buffer size */
dword isRtr = 0;                                /* specifies if the message is a rtr frame */
dword transmitCounter = 0;                      /* indicate the position */
dword replace = 0;                              /* insert or replace */
dword index = 0x2001;                           /* object index */
dword subIndex = 0;                             /* object sub-index */
dword size = 0;                                 /* size of data in bytes */
byte inValueBuf[5] = {0x0, 0x0, 0x0, 0x0, 0x0}; /* data */
dword valueBufSize = 5;                         /* buffer size */
char msg[100];

/* Tip:
  * For the used object [0x2001,0x0] is assumed:
  * - that it exits and it is writable
  * - that it can receive 5 bytes for a normal transfer
  *
  * In this example is expected, that the DUT aborts the transfer.
  * The function coTfsSDOInjectRawMsg inserts a invalid messages in the sequence
*/

retValFunc = kTestStepPassed;
msg[0] = '\0';

/* Set the node-ID of DUT */
strncpy(msg,"Set node-ID", elCount(msg));
retValFunc = coTfsSetNodeId(nodeId);

/* reset abort list */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsSDOResetAbortList - before", elCount(msg));
  retValFunc = coTfsSDOResetAbortList(0);
} /* if */

/* reset accepted abort list */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsSDOResetAccAbortList - before", elCount(msg));
  retValFunc = coTfsSDOResetAccAbortList();
} /* if */

/* add accepted abort code to list */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsSDOAddAccAbortCode - Client/server command specifier not valid or unknown", elCount(msg));
  retValFunc = coTfsSDOAddAccAbortCode(0x05040001);
} /* if */

/* add accepted abort code to list */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsSDOAddAccAbortCode - general error", elCount(msg));
  retValFunc = coTfsSDOAddAccAbortCode(0x08000000);
} /* if */

/* prepare data for injection */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsSDOInjectRawMsg - Init block upload", elCount(msg));
  msgCanId = 0x600 + nodeId;
  msgDlc = 8;
  buf[0] = 0xA4;
  buf[1] = 0x17;
  buf[2] = 0x10;
  buf[3] = 0x00;
  buf[4] = 0x01;
  buf[5] = 0x00;
  buf[6] = 0x00;
  buf[7] = 0x00;
  bufSize = 8;
  isRtr = 0;
  transmitCounter = 1;
  replace = 1;
  retValFunc = coTfsSDOInjectRawMsg( msgCanId /*dword canId*/, msgDlc /*dword dlc*/, buf /*byte buf[]*/, bufSize /*dword bufSize*/, isRtr /*dword isRtr*/, transmitCounter /*dword transmitCounter*/, replace /*dword replace*/ );
} /* if */

/* perform a download */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsSDODownload", elCount(msg));
  retValFunc = coTfsSDODownload( index /*dword index*/, subIndex /*dword subIndex*/, size /*dword size*/, inValueBuf /*byte inValueBuf[]*/, valueBufSize /*dword valueBufSize*/ );
} /* if */

/* reset abort list */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsSDOResetAbortList - after", elCount(msg));
  retValFunc = coTfsSDOResetAbortList(0);
} /* if */

/* reset accepted abort list */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsSDOResetAccAbortList - after", elCount(msg));
  retValFunc = coTfsSDOResetAccAbortList();
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
