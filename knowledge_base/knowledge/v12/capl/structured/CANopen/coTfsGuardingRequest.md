# coTfsGuardingRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsGuardingRequest( dword guardTime, dword retryFactor, dword tolerance, dword guardReqNumber, dword waitForEmcy );
```

## Description

The test sets the guard time and retry factor objects in the DUT Device Under Test. After that, guardReqNumber remote guarding frames are sent to the target device. The target device must respond to each individual query within the tolerance delta. The test run is sequential.

After that, the sending of the guarding remote frames is stopped. Depending on the waitForEmcy setting, it is waited for an emergency message (coTfsSetTimeoutValue ) before guard time and retry factor are reset again.

An eventually existing active heartbeat producer is disabled at test start and enabled again at the end of the test.

## Return Values

Error code

## Example

```c
long retValFunc = kTestStepPassed; /* to store the return value of function */
long nodeId = 112;                 /* Node-Id of DUT */

dword guardTime = 500;         /* guard time */
dword retryFactor = 5;         /* life time factor */
dword tolerance = 50;          /* tolerance for the measure */
dword guardReqNumber = 100;    /* number of guard request */
dword waitForEmcy = 1;         /* if emcy message expected */
char msg[100];                 /* message */

retValFunc = kTestStepPassed;
msg[0] = '\0';

/* Set the node-ID of DUT */
strncpy(msg,"Set node-ID", elCount(msg));
retValFunc = coTfsSetNodeId(nodeId);

/* call test function */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsGuardingRequest", elCount(msg));
  retValFunc = coTfsGuardingRequest( guardTime, retryFactor, tolerance, guardReqNumber, waitForEmcy );
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
