# coTfsSDOInit

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOInit( dword index, dword subIndex, dword ccs, dword expedited, dword sizeIndicated, dword notUsed, byte inValueBuf[], dword valueBufSize );
```

## Description

This function sends an initialization message for

The protocol is described in detail in DS-301.

## Parameters

| Name | Description |
|---|---|
| index | Object index |
| subIndex | Object sub index |
| ccs (client command specifier) | 1: download 2: upload, other values can cause unexpected behavior |
| expedited | 0: normal transfer 1: expedited transfer |
| sizeIndicated | 0: size unknown 1: size known (recommended value) |
| notUsed | Number of data bytes that contain no reference data. |
| inValueBuf[] | Data field, at least 4 bytes large reference data assigned. |
| valueBufSize | Buffer size in byte of inValueBuf. |

## Return Values

Error code

## Example

```c
const int kTestStepPassed = 1;     /* to indicate a successfuly execution */
long retValFunc = kTestStepPassed; /* to store the return value of function */

long nodeId = 112;            /* Node-Id of DUT */
dword index = 0x1017;         /* object index, manufacturer device name */
dword subIndex = 0;           /* object sub-index */
dword ccs = kClientCommandSpecifier_InitiateUploadRequest;
dword expedited = 0;          /* it does not matter for upload */
dword sizeIndicated = 0;     /* it does not matter for upload */
dword notUsed = 0;           /* it does not matter for upload */
byte inValueBuf[1] = {0x0};  /* it does not matter for upload */
dword valueBufSize = 1;      /* it does not matter for upload */
dword dataLength = 0;        /* to store the return value of coTfsSDOGetUploadSize */
dword dataLengthCounter = 0; /* to store the remain length of data to be uploaded */
byte outValueBuf[100];       /* to store the uploaded data */
dword outvalueBufSize = 100; /* buffer size */
dword cont = 1;              /* continue bit */
dword toggleBit = 0;         /* toggle bit */
char msg[100];               /* message */
retValFunc = kTestStepPassed;
msg[0] = '\0';

/* Set the node-ID of DUT */
strncpy(msg,"Set node-ID", elCount(msg));
retValFunc = coTfsSetNodeId(nodeId);

/* Tip:
  * Using the level 2 function for upload :
  * dword size = 2; // size of data in bytes
  * coTfsSDOUpload( index, subIndex );
*/

/* initiate upload trasnfer */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsSDOInit", elCount(msg));
  ccs = kClientCommandSpecifier_InitiateUploadRequest;
  expedited = 0;       /* it does not matter for upload */
  sizeIndicated = 0;   /* it does not matter for upload */
  notUsed = 0;         /* it does not matter for upload */
  inValueBuf[0] = 0x0; /* it does not matter for upload */
  valueBufSize = 1;    /* it does not matter for upload */
  retValFunc = coTfsSDOInit( index /*dword index*/, subIndex /*dword subIndex*/, ccs /*dword ccs*/, expedited /*dword expedited, it does not matter for upload */, sizeIndicated /*dword sizeIndicated, it does not matter for upload */, notUsed /*dword notUsed, it does not matter for upload */, inValueBuf /*byte inValueBuf[], it does not matter for upload */, 0 /*dword valueBufSize, it does not matter for upload */ );
} /* if */

/* request segment if the size of data is greater then 4 bytes */
if (retValFunc == kTestStepPassed)
{
  /* get the size data coming from SDO server */
  dataLength = coTfsSDOGetUploadSize();
  /* outputs a message to the 'write' window */
  write( "coTfsSDOGetUploadSize = %X", dataLength);
  /* determinate if a segmented transfer has to be started */
  /* normal transfer - request segment */
  if (dataLength > 4)
  {
    strncpy(msg,"coTfsSDOSegmentRequest", elCount(msg));
    dataLengthCounter = dataLength;
    toggleBit = 0; /* toggle bit */

    /* get the data */
    while ((retValFunc == kTestStepPassed) && (dataLengthCounter > 0))
    {
      /* normal transfer */
      ccs = kClientCommandSpecifier_UploadSegmentRequest;
      toggleBit &= 0x0001; /* toggle bit */
      notUsed = 0; /* it does not matter for upload */
      inValueBuf[0] = 0x0; /* it does not matter for upload */
      valueBufSize = 1; /* it does not matter for upload */
      retValFunc = coTfsSDOSegmentRequest( ccs /*dword ccs*/, cont /*dword cont*/, toggleBit /*dword toggleBit*/, notUsed /*dword notUsed*/, inValueBuf /*byte inValueBuf[]*/, valueBufSize /*dword valueBufSize*/ );

      /* set next toggle */
      toggleBit++;

      /* This example assumes, that the SDO server does not send empty segments, n=0*/
      /* determinate remain length */
      if (dataLengthCounter - 7 >= 0)
      {
        dataLengthCounter -= 7;
      }
      else
      {
        dataLengthCounter = 0;
      } /* else*/
    } /* while */
  } /* if */
} /* if */

/* request segment if the size of data is greater then 4 bytes */
if (retValFunc == kTestStepPassed)
{
  /* get the size data coming from SDO server */
  dataLength = coTfsSDOGetUploadSize();
  /* outputs a message to the 'write' window */
  write( "coTfsSDOGetUploadSize = %X", dataLength);
  /* determinate if a segmented transfer has been started */
  dataLength = coTfsSDOGetUploadData( outValueBuf /*byte outValueBuf[]*/, outvalueBufSize /*dword valueBufSize*/ );
  if (dataLength > 0)
  {
    /* outputs a failure message to the 'write' window */
    write( "Length of data bytes returned with coTfsSDOGetUploadData = 0x%X", dataLength);
    write( "First received data byte = 0x%X", outValueBuf[0]);
    write( "Last received data byte = 0x%X", outValueBuf[dataLength-1]);
  }
  else
  {
    strncpy(msg,"coTfsSDOGetUploadData", elCount(msg));
    retValFunc = (!kTestStepPassed);
  } /* else */
} /* else */

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
