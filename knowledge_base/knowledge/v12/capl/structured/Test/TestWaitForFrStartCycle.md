# TestWaitForFrStartCycle

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForFrStartCycle (dword aCycle, dword aTimeout);
```

## Description

Waits for the occurrence of the specified FlexRay start cycle event. Should the event not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

When no numeric cycle is specified the wait condition is resolved on any FlexRay Start Cycle event.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

## Example

The following test program waits for the occurrence of one of two different start of cycles.

It is assumed that the test is executed at the cluster FlexRay A.

```c
variables
{
   dword gBusContextFr1;
   long resTestWaitFor, resTestGetData, resTestJoin;
   dword timeToWait  = 100; // in ms
   const dword gCycleOffset1 = 2;
   const dword gCycleRepetition1 = 4;
   const dword gCycleOffset2 = 3;
   const dword gCycleRepetition2 = 4;
}
void InitBusContext ()
{
   gBusContextFr1 = getBusNameContext("FlexRay A");
   SetBusContext(gBusContextFr1);
}
testcase WaitForJoinedFrStartCycle_Any()
{
   FrStartCycle frStartCycleData;
   InitBusContext();
   // join events
   {
      TestStepPass("Call TFS function", "TestJoinFrStartCycleEvent(CycleOffset=%d, CycleRepetition=%d)",
                    gCycleOffset1, gCycleRepetition1);
      resTestJoin = TestJoinFrStartCycleEvent(gCycleOffset1, gCycleRepetition1);
      if (resTestJoin <= 0)
      {
         TestStepFail("Join condition", "resTestJoin = %d, Failure on joining multi-cycle event", resTestJoin);
         return;
      }
      else
      {
         TestStepPass("Join condition", "Joining multi-cycle event ok. Event number = %d", resTestJoin);
      }
      TestStepPass("Call TFS function", "TestJoinFrStartCycleEvent(CycleOffset=%d, CycleRepetition=%d)",
                    gCycleOffset2, gCycleRepetition2);
      resTestJoin = TestJoinFrStartCycleEvent(gCycleOffset2, gCycleRepetition2);
      if (resTestJoin <= 0)
      {
         TestStepFail("Join condition", "resTestJoin = %d, Failure on joining single-cycle event", resTestJoin);
         return;
      }
      else
      {
         TestStepPass("Join condition", "Joining single-cycle event ok. Event number = %d", resTestJoin);
      }
   }
   // wait for any event
   TestStepPass("Call TFS function", "TestWaitForAnyJoinedEvent(timeout=%d)", timeToWait);
   resTestWaitFor = TestWaitForAnyJoinedEvent(timeToWait);
   if (resTestWaitFor > 0) // Resume due to event occurred
   {
      TestStepPass("Wait condition", "Waiting for any joined event is ok. Resume event number = %d", resTestWaitFor);
      TestStepPass("Call TFS function", "TestGetWaitFrStartCycleData(index=%d, frStartCycleData)", resTestWaitFor);
      
      // extract resume event's data
      resTestGetData = TestGetWaitFrStartCycleData(resTestWaitFor, frStartCycleData);
      if (0 != resTestGetData)
      {
         TestStepFail("Data extraction", "resTestGetData = %d, Data access to data of event %d could not be executed!", resTestGetData, resTestWaitFor);
      }
      else
      {
         TestStepPass("Data extraction", "Data of event %d succefully extracted. CycleId=%d", resTestWaitFor, frStartCycleData.FR_Cycle);
      }
   }
   else
   {
      TestStepFail("Wait condition", "resTestWaitFor = %d, Waiting for any joined event failed!", resTestWaitFor);
   }
}
```

## Availability

| Since Version |
|---|
