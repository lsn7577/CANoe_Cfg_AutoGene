# TestWaitForFrFrame

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForFrFrame (dbFrFrame aFrame, dword aTimeout);
```

## Description

Waits for the occurrence of the valid specified FlexRay frame. Should the frame not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

When no frame is specified the wait condition is resolved on any valid FlexRay frame.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

## Example

The following test program waits for the occurrence of one of two frames.

It is assumed that the database defines the frames Sync_Message_1_Ch_A and Sync_Message_2_Ch_A on the cluster FlexRay A.

```c
variables
{
   dword gBusContextFr1;
   long resTestWaitFor, resTestGetData, resTestJoin;
   dword timeToWait  = 10; // in ms
}
void InitBusContext ()
{
   gBusContextFr1 = getBusNameContext("FlexRay A");
   SetBusContext(gBusContextFr1);
}
testcase WaitForJoinedFrFrames_Any()
{
   FrFrame Sync_Message_1_Ch_A frTest1;
   FrFrame Sync_Message_2_Ch_A frTest2;
   InitBusContext();
   // join events
   {
      TestStepPass("Call TFS function", "TestJoinFrFrameEvent(Sync_Message_1_Ch_A) for (SlotId=%d, BaseCycle=%d, Repetition=%d)",
                    frTest1.FR_SlotID, frTest1.FR_CycleOffset, frTest1.FR_CycleRepetition);
      resTestJoin = TestJoinFrFrameEvent(Sync_Message_1_Ch_A);
      if (resTestJoin <= 0)
      {
         TestStepFail("Join condition", "resTestJoin = %d, Failure on joining symbolic event", resTestJoin);
         return;
      }
      else
      {
        TestStepPass("Join condition", "Joining symbolic event ok. Event number = %d", resTestJoin);
      }
      TestStepPass("Call TFS function", "TestJoinFrFrameEvent(SlotId=%d, BaseCycle=%d, Repetition=%d,...)",
                    frTest2.FR_SlotID, frTest2.FR_CycleOffset, frTest2.FR_CycleRepetition);
      resTestJoin = TestJoinFrFrameEvent(frTest2.FR_SlotID, frTest2.FR_CycleOffset, 
                                         frTest2.FR_CycleRepetition, frTest2.FR_ChannelMask);
      if (resTestJoin <= 0)
      {
         TestStepFail("Join condition", "resTestJoin = %d, Failure on joining raw event", resTestJoin);
         return;
      }
      else
      {
         TestStepPass("Join condition", "Joining raw event ok. Event number = %d", resTestJoin);
      }
   }
   TestStepPass("Call TFS function", "TestWaitForAnyJoinedEvent(timeout = %d)", timeToWait);
   // wait for any event
   resTestWaitFor = TestWaitForAnyJoinedEvent(timeToWait);
   if (resTestWaitFor > 0) // Resume due to event occurred
   {
      TestStepPass("Call TFS function", "TestGetWaitFrFrameData(resTestWaitFor=%d, frTest)", resTestWaitFor);
      // extract resume event's data
      resTestGetData = TestGetWaitFrFrameData(resTestWaitFor, frTest1);
      if (0 != resTestGetData)
      {
         TestStepFail("Data extraction", "resTestGetData = %d, Data access to data of event %d could not be executed!", resTestGetData, resTestWaitFor);
      }
      else
      {
         TestStepPass("Data extraction", "Data of event %d succefully extracted. SlotId=%d", resTestWaitFor, frTest1.FR_SlotID);
      }
   }
   else
   {
      TestStepFail("Wait condition", "resTestWaitFor = %d, Waiting for any of joined events during %d [ms] failed!", resTestWaitFor, timeToWait);
   }
}
```

## Availability

| Since Version |
|---|
