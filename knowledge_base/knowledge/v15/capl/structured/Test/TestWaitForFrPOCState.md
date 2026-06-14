# TestWaitForFrPOCState

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForFrPOCState (dword aTimeout);
long TestWaitForFrPOCState (dword aPOCState, dword aTimeout);
long TestWaitForFrPOCState (dword aPOCState, dword aWUState, dword aTimeout);
```

## Description

Waits for the occurrence of change of state on the FlexRay Communication Controller's protocol operation state machine. Should the change not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

## Parameters

| Name | Description |
|---|---|
| aTimeout | Maximum time that should be waited [ms] (Transmission of 0: no timeout controlling) |
| aPOCState | The POC state the function will wait for (see selector 'FR_POCState' in event procedure on FrPOCState). If set to '-1' in combination with a 'WUState' the function will wait only for a Wakeup state (any POC state will be accepted). Available from CANoe 7.2. |
| aWUState | The Wakeup state the function will wait for (see selector 'FR_Info2' in event procedure on FrPOCState). Available from CANoe 7.2. |

## Example

The following test program waits for the occurrence of one of two different POC state events.

It is assumed that the test is executed at the cluster FlexRay A.

```c
variables
{
   dword gBusContextFr1;
   long resTestWaitFor, resTestGetData, resTestJoin;
   dword timeToWait  = 1000; // in ms
   const int flexrayChannel = %CHANNEL%; // used by CAPL functions stimulating events
}
void InitBusContext ()
{
   gBusContextFr1 = getBusNameContext("FlexRay A");
   SetBusContext(gBusContextFr1);
}
testcase WaitForJoinedFrPOCState_Any()
{
   FrPOCState frPOCStateData;
   InitBusContext();
   // join events
   {
      TestStepPass("Call TFS function", "TestJoinFrPOCState()");
      resTestJoin = TestJoinFrPOCState();
      if (resTestJoin <= 0)
      {
         TestStepFail("Join event", "resTestJoin = %d, Failure on joining first multi-cycle event", resTestJoin);
         return;
      }
      else
      {
         TestStepPass("Join event", "Joining first multi-cycle event ok. Event number = %d", resTestJoin);
      }
      TestStepPass("Call TFS function", "TestJoinFrPOCState()");
      resTestJoin = TestJoinFrPOCState();
      if (resTestJoin <= 0)
      {
         TestStepFail("Join event", "resTestJoin = %d, Failure on joining second multi-cycle event", resTestJoin);
         return;
      }
      else
      {
         TestStepPass("Join event", "Joining second multi-cycle event ok. Event number = %d", resTestJoin);
      }
   }
   StimulatePOCEvent();
   // wait for any event
   TestStepPass("Call TFS function", "TestWaitForAnyJoinedEvent(timeout=%d)", timeToWait);
   resTestWaitFor = TestWaitForAnyJoinedEvent(timeToWait);
   if (resTestWaitFor > 0) // Resume due to event occurred
   {
      TestStepPass("Wait condition", "Waiting for any joined event is ok. Resume event number = %d", resTestWaitFor);
      TestStepPass("Call TFS function", "TestGetWaitFrPOCStateData(index=%d, frPOCStateData)", resTestWaitFor);
      
      // extract resume event's data
      resTestGetData = TestGetWaitFrPOCStateData(resTestWaitFor, frPOCStateData);
      if (0 != resTestGetData)
      {
         TestStepFail("Data extraction", "resTestGetData = %d, Data access to data of event %d could not be executed!", resTestGetData, resTestWaitFor);
      }
      else
      {
         TestStepPass("Data extraction", "Data of event %d succefully extracted. StateCode=%d", resTestWaitFor, frPOCStateData.FR_POCState);
      }
   }
   else
   {
      TestStepFail("Wait condition", "resTestWaitFor = %d, Waiting for any joined event failed!", resTestWaitFor);
   }
}
void StimulatePOCEvent ()
{
  ResetFlexRayCC(flexrayChannel); // stimulate one POC event
  TestStepPass("Event stimulation", "POC event(s) stimulated with ResetFlexRayCC(channel=%d)", flexrayChannel);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 SP4 7.2: extended | 13.0 | — | — | 1.0 |
| Restricted To | — | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
