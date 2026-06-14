# coTfsSDOBlockInit

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOBlockInit( dword index, dword subIndex, dword ccs, dword cs, dword crcSupported, dword sizeIndicated, dword blkSize, dword size, dword threshold );
```

## Description

This function starts a SDO block download or SDO block upload and waits for the corresponding response.

## Return Values

Error code

## Example

```c
const int kTestStepPassed = 1;      /* to indicate a successful execution */
long retValFunc = kTestStepPassed;  /* to store the return value of function */

long nodeId = 112;     /* Node-Id of DUT */
dword index = 0x1017;  /* object index */
dword subIndex = 0;    /* object sub-index */
dword ccs = kClientCommandSpecifier_BlockUpload;
dword cs = kClientSubcommand_InitiateUploadRequest;
dword crcSupported = kCRC_Support;
dword blkSize = 1;          /* Number of segments per block */
dword threshold = 0;        /* Change of transfer protocol not allowed */
dword sizeIndicated = 0;    /* it does not matter for upload transfer */
dword size = 0;             /* it does not matter for upload transfer */
dword ackSeq = 0;           /* acknowledge sequence number */
dword expMsgNumber = 0;     /* to specify the number of expected messages */
dword startSeqNumber = 0;   /* to indicate the start value of sequence number */
dword notUsed = 0;          /* number of bytes, which does not contains data */
dword crc = 0;              /* crc value */
dword crcSupportFlag = 0;   /* to store the return value of coTfsSDOChkCrcSupport */
dword dataLength = 0;       /* to store the return value of coTfsSDOGetUploadSize */
dword crcSetting = 2;       /* no information about CRC support, received CRC are not evaluated */
dword receivedCRC[1] = {0}; /* to store the returned CRC value from SDO server */
char msg[100];              /* message */
retValFunc = kTestStepPassed;
msg[0] = '\0';
receivedCRC[0]=0;

/* Set the node-ID of DUT */
strncpy(msg,"Set node-ID", elCount(msg));
retValFunc = coTfsSetNodeId(nodeId);

/* Tip:
  * Using the level 2 function for block upload transfer :
  * dword useCrc = 0;
  * dword outCrcUsed[1] = {0};
  * coTfsSDOBlockUpload(index, subIndex, useCrc, outCrcUsed);
*/

/* initiate upload request */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsSDOBlockInit - initiate upload request", elCount(msg));
  cs = kClientSubcommand_InitiateUploadRequest; /* 0 initiate upload request */
  retValFunc = coTfsSDOBlockInit( index, subIndex, ccs, cs, crcSupported, sizeIndicated, blkSize, size, threshold );

  /* check if the sdo server supports CRC */
  crcSupportFlag = coTfsSDOChkCrcSupport();

  /* outputs a message to the 'write' window */
  write( "coTfsSDOChkCrcSupport = %X", crcSupportFlag);

  /* Get the length of data to be uploaded */
  dataLength = coTfsSDOGetUploadSize();

  /* outputs a message to the 'write' window */
  write( "Length of data to be uploaded = %d", dataLength);
} /* if */

/* start block upload */
if (retValFunc == kTestStepPassed)
{
  /* start block upload */
  strncpy(msg,"coTfsSDOBlockInit - start block upload", elCount(msg));
  ccs = kClientCommandSpecifier_BlockUpload; /* block upload */ 
  cs = kClientSubcommand_StartUpload;

  /* start upload */ retValFunc = coTfsSDOBlockInit( 0 /*dword index*/, 0 /*dword subIndex*/, ccs /*dword ccs*/, cs /*dword cs*/, 0 /*dword crcSupported*/, 0 /*dword sizeIndicated*/, 0 /*dword blkSize*/, 0 /*dword size*/, 0 /*dword threshold*/ );
} /* if */

/* request segment */
if (retValFunc == kTestStepPassed)
{
  /* wait for the data */
  testWaitForTimeout(10);

  /* Acknowgleg the last block and seq. number */
  strncpy(msg,"coTfsSDOBlockUploadSegmentResponse", elCount(msg));
  ccs = kClientCommandSpecifier_BlockUpload; /* block upload */
  cs = kClientSubcommnad_BlockUploadResponse; /* block upload response */
  ackSeq = 1; /* acknowledge seq. number */
  startSeqNumber = 1; /* expected start of seq. number from SDO server */
  retValFunc = coTfsSDOBlockUploadSegmentResponse( ccs /*dword ccs*/, cs /*dword cs*/, ackSeq /*dword ackSeq*/, blkSize /*dword blkSize*/, expMsgNumber /*dword expMsgNumber*/, startSeqNumber /*dword startSeqNumber*/ );
} /* if */

/* end block upload */
if (retValFunc == kTestStepPassed)
{
  /* determinate the number of bytes, which does not contains data */
  notUsed = (7 - (dataLength % 7));

  /* outputs a message to the 'write' window */
  write( "notUsed %X", notUsed);

  /* End the block transfer */
  strncpy(msg,"coTfsSDOBlockEnd", elCount(msg));
  ccs = kClientCommandSpecifier_BlockUpload; /* block upload */
  cs = kClientSubcommnad_EndBlockUploadRequest; /* end block upload request */
  retValFunc = coTfsSDOBlockEnd( ccs /*dword ccs*/, cs /*dword cs*/, notUsed /*dword notUsed*/, 0 /*dword crc*/, crcSetting /*dword crcSetting*/ );
} /* if */

/* end block upload */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsSdoBlockUploadGetCRC", elCount(msg));
  retValFunc = coTfsSdoBlockUploadGetCRC(receivedCRC);

  /* outputs a message to the 'write' window */
  write( "received CRC = 0x%X", receivedCRC[0]);
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
