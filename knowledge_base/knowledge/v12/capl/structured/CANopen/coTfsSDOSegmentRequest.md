# coTfsSDOSegmentRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOSegmentRequest( dword ccs, dword cont, dword toggleBit, dword notUsed, byte inValueBuf[], dword valueBufSize );
```

## Description

This function sends a SDO segmented download or SDO segmented upload request/response and awaits the corresponding response. The DS-301 describes the precise protocol and all parameters.

## Return Values

Error code

## Example

```c
long retValFunc = kTestStepPassed; /* to store the return value of function */

long nodeId = 112;                         /* Node-Id of DUT */
dword index = 0x1017;                      /* object index */
dword subIndex = 0;                        /* object sub-index */
dword ccs = kClientCommandSpecifier_InitiateDownloadRequest;
dword expedited = kTransfer_Normal;
dword sizeIndicated = kSize_Indicated;
dword notUsed = 0;                         /* no of byte without data */
byte inValueBuf[4] = {0x2, 0x0, 0x0, 0x0}; /* length of data to be downloaded */
dword valueBufSize = 4;                    /* buffer size */
dword cont = kContinueBit_NoMoreSegments;
dword toggleBit = 0;                       /* toggle bit */
char msg[100];                             /* message */
retValFunc = kTestStepPassed;
msg[0] = '\0';

/* Set the node-ID of DUT */
strncpy(msg,"Set node-ID", elCount(msg));
retValFunc = coTfsSetNodeId(nodeId);
/* Tip:
  * Using the level 2 function for download :
  * dword size = 2; // size of data in bytes
  * coTfsSDODownload( index, subIndex, size,inValueBuf, valueBufSize );
*/

/* initiate download request */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsSDOInit", elCount(msg));
  ccs = kClientCommandSpecifier_InitiateDownloadRequest;
  expedited = kTransfer_Normal;
  sizeIndicated = kSize_Indicated;
  notUsed = 3; /* number of bytes does not contains data bytes */
  inValueBuf[0] = 0x2;
  inValueBuf[1] = 0x0;
  inValueBuf[2] = 0x0;
  inValueBuf[3] = 0x0;
  retValFunc = coTfsSDOInit( index /*dword index*/, subIndex /*dword subIndex*/, ccs /*dword ccs*/, expedited /*dword expedited*/, sizeIndicated /*dword sizeIndicated*/, notUsed /*dword notUsed*/, inValueBuf /*byte inValueBuf[]*/, valueBufSize /*dword valueBufSize*/ );
} /* if */

/* download segment request */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsSDOSegmentRequest", elCount(msg));
  inValueBuf[0] = 0x0;
  inValueBuf[1] = 0x0;
  inValueBuf[2] = 0x0;
  inValueBuf[3] = 0x0;
  ccs = kClientCommandSpecifier_DownloadSegmentRequest;
  cont = kContinueBit_NoMoreSegments;
  toggleBit = 0; /* toggle bit */
  notUsed = 5; /* number of bytes does not contains data bytes */
  retValFunc = coTfsSDOSegmentRequest( ccs /*dword ccs*/, cont /*dword cont*/, toggleBit /*dword toggleBit*/, notUsed /*dword notUsed*/, inValueBuf /*byte inValueBuf[]*/, valueBufSize /*dword valueBufSize*/ );
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
