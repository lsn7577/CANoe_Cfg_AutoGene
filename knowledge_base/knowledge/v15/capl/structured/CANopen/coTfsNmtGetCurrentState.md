# coTfsNmtGetCurrentState

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsNmtGetCurrentState( dword nmtState[1] );
```

## Description

This function returns the current device status of the DUT Device Under Test. The current state is checked with heartbeat and guarding mechanisms.

For this, there is first an attempt to configure a heartbeat producer in the DUT (object 0x1017). The heartbeat message contains the current device status. If the DUT should not make a heartbeat producer available, a remote guarding frame is sent to the DUT. The DUT responds with the corresponding guarding response. The procedure is repeated again. The second response is evaluated and contains the device status. The CANopen® specification provides that a CANopen® device supports at least one of the two modes.

## Parameters

| Name | Description |
|---|---|
| nmtState | Current device status (data field) 0: boot-up 4: stopped 5: operational 127: pre-operational |

## Return Values

Error code

## Example

```c
long retValFunc = kTestStepPassed; /* to store the return value of function */
long nodeId = 112;                 /* Node-Id of DUT */

dword nmtState[1] = 0;
char msg[100]; /* message */
retValFunc = kTestStepPassed;
msg[0] = '\0';

/* Set the node-ID of DUT */
strncpy(msg,"Set node-ID", elCount(msg));
retValFunc = coTfsSetNodeId(nodeId);

/* call test function */
if (retValFunc == kTestStepPassed)
{
  strncpy(msg,"coTfsNMTGetCurrentState", elCount(msg));
  retValFunc = coTfsNmtGetCurrentState( nmtState );

  /* evaluation of returned value */
  switch(nmtState[0])
  {
    case kNMTState_BootUp : /* Initialization/Boot-up */
    {
      write( "DUT is in NMT state Initialization/Boot-up");
      break;
    } /* case */
    case kNMTState_Stopped : /* Stopped */
    {
      write( "DUT is in NMT state Stopped");
      break;
    } //* case */
    case kNMTState_Operationa1 : /* Operational */
    {
      write( "DUT is in NMT state Operational");
      break;
    } /* case */
    case kNMTState_PreOperational : /* Pre-operational */
    {
      write( "DUT is in NMT state Pre-operational");
      break;
    } /* case */
  } /* switch */
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
