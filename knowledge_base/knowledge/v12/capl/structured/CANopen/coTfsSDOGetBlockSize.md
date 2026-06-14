# coTfsSDOGetBlockSize

> Category: `CANopen` | Type: `function`

## Syntax

```c
dword coTfsSDOGetBlockSize( void );
```

## Description

The function returns the block size of the last Initiate SDO Block Download or Download SDO Block Segment Response message.

With a return value 0, the message is not detected or awaited. The block size can only be read out once after each individual block

## Return Values

Block size

## Example

```c
long retValFunc = kTestStepPassed; /* to store the return value of function */
long nodeId = 112;                 /* Node-Id of DUT */

dword index = 0x1017; /* object index */
dword subIndex = 0;   /* object sub-index */
dword ccs = kClientCommandSpecifier_BlockDownload;
dword cs = kClientSubcommand_InitiateDownloadRequest;
dword crcSupported = kCRC_Support; /* 1 = client supports CRC check */
dword sizeIndicated = 1;           /* 1 = size known */
dword size = 2;                    /* size of the data transmission in bytes */
dword blkSize = 0;                 /* It does not matter for block download transfer */
dword threshold = 0;               /* It does not matter for block download transfer */
dword crcSupportFlag = 0;          /* to store the return value of coTfsSDOChkCrcSupport */
dword newBlkSize = 0;              /* to store the return value of coTfsSDOGetBlockSize */
dword cont = kContinueBit_NoMoreSegments;
dword seqNumber = 1;               /* sequence number */
byte inValueBuf[2] = {0, 0};       /* data to be downloaded */
dword valueBufSize = 2;
dword isLastSegment = 1;           /* It is the last segment for the current block transfer, 0 = do not wait for block confirmation, 1 = wait for block confirmation */
dword notUsed = 0;                 /* number of bytes, which does not contains data */
dword crc = 0;                     /* crc value */
char msg[100];                     /* message */
retValFunc = kTestStepPassed;
msg[0] = '\0';

/* Set the node-ID of DUT */
strncpy(msg,"Set node-ID", elCount(msg));
retValFunc = coTfsSetNodeId(nodeId);

/* Tip: Using the level 2 function for block download transfer :
  * dword useCrc = 1;
  * dword outCrcUsed[1] = {0};
  * coTfsSDOBlockDownload(index, subIndex, size, 1, inValueBuf, valueBufSize, outCrcUsed);
*/

/* initiate block download request */
if (retValFunc == kTestStepPassed)
{
  /* initiate the block download */
  strncpy(msg,"coTfsSDOBlockInit", elCount(msg));
  retValFunc = coTfsSDOBlockInit( index, subIndex, ccs, cs, crcSupported, sizeIndicated, blkSize, size, threshold );
} /* if */

/* block download segment request */
if (retValFunc == kTestStepPassed)
{
  /* check if the sdo server supports CRC */
  crcSupportFlag = coTfsSDOChkCrcSupport();
  /* outputs a message to the 'write' window */
  write( "coTfsSDOChkCrcSupport = %X", crcSupportFlag);
  /* get the block size data coming from SDO server */
  newBlkSize = coTfsSDOGetBlockSize();/* outputs a message to the 'write' window */
  write( "coTfsSDOGetBlockSize = %X", newBlkSize);
  /* send segment data to SDO server */
  strncpy(msg,"coTfsSDOBlockDownloadSegmentRequest", elCount(msg));
  retValFunc = coTfsSDOBlockDownloadSegmentRequest( cont, seqNumber, inValueBuf, valueBufSize, isLastSegment );
} /* if */

/* block download segment request */
if (retValFunc == kTestStepPassed)
{
  /* calculate the CRC */
  crc = coTfsSDOCalcCrc( inValueBuf, valueBufSize );
  /* outputs a message to the 'write' window */
  write( "coTfsSDOCalcCrc = %X", crc);
  /* end the block download transfer */
  strncpy(msg,"coTfsSDOBlockEnd", elCount(msg));
  ccs = 6; /* 6 = block download */
  cs = 1; /* end block download */
  notUsed = 5; /* number of bytes in the last segment that contains no data */
  retValFunc = coTfsSDOBlockEnd( ccs, cs, notUsed, crc );
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
