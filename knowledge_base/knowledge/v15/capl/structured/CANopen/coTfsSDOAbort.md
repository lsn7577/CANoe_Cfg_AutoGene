# coTfsSDOAbort

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOAbort( dword index, dword subIndex, dword abortCode );
```

## Description

This function sends out a SDO abort message.

## Parameters

| Name | Description |
|---|---|
| index | Object index |
| subIndex | Object sub index |
| abortCode | Abort code |

## Return Values

Error code

## Example

```c
long retValFunc = kTestStepPassed; /* to store the return value of function */
long nodeId = 112;                 /* Node-Id of DUT */

dword index = 0x1017; /* object index */
dword subIndex = 0;   /* object sub-index */
dword ccs = kClientCommandSpecifier_InitiateDownloadRequest;
dword expedited = kTransfer_Normal;
dword sizeIndicated = kSize_Indicated;
dword notUsed = 0; /* no of byte without data */
byte inValueBuf[4] = {0x2, 0x0, 0x0, 0x0}; /* length of data to be downloaded */
dword valueBufSize = 4;
dword abortCode = 0;
char msg[100];
retValFunc = kTestStepPassed;
msg[0] = '\0';

/* Set the node-ID of DUT */
strncpy(msg,"Set node-ID", elCount(msg));
retValFunc = coTfsSetNodeId(nodeId);

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
  strncpy(msg,"coTfsSDOAbort", elCount(msg));
  abortCode = 0x08000000; /* general error */
  retValFunc = coTfsSDOAbort( index /*dword index*/, subIndex /*dword subIndex*/, abortCode /*dword abortCode*/ );
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
