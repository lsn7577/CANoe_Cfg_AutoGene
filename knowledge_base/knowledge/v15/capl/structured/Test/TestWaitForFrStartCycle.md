# TestWaitForFrStartCycle

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForFrStartCycle (dword aCycle, dword aTimeout);
long TestWaitForFrStartCycle (dword aBaseCycle, dword aCycleRepetition, dword aTimeout);
long TestWaitForFrStartCycle (dword aTimeout);
```

## Description

Waits for the occurrence of the specified FlexRay start cycle event. Should the event not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

When no numeric cycle is specified the wait condition is resolved on any FlexRay Start Cycle event.

## Parameters

| Name | Description |
|---|---|
| aCycle | Numeric cycle identifier. 0...63 |
| aBaseCycle | Numeric base cycle. This value must be less than the repetition factor. Together with the repetition factor this value determines the "Cycle Multiplexing". Value range: 0...63 |
| aCycleRepetition | Cycle repetition factor. Together with the base cycle this value determines the "Cycle Multiplexing". Value has to be a power to 2 (1, 2, 4, 8, 16, 32 or 64). |
| aTimeout | Maximum time that should be waited [ms] (Transmission of 0: no timeout controlling) |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 SP4 | 13.0 | — | — | 1.0 |
| Restricted To | — | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
