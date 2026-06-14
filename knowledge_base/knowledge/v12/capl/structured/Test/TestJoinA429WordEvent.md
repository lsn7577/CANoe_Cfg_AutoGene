# TestJoinA429WordEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinA429WordEvent (dbA429Word aWord )
```

## Description

Add an ARINC word to the set of joined events. If ARINC word events are delivered from different buses, the context has to be adjusted correctly (SetBusContext). The function does not wait and handles only incoming and error free ARINC words.

## Return Values

-3: Join error

## Example

```c
//Example
//This example creates a join for two messages on different buses and waits for any of them. After successful reception of one the messages, the data of this message is extracted.
variables
{
  dword a429Ch5Context = 0;
  dword a429Ch6Context = 0;
  long resultTestJoin = 0;
  long resultTestWaitFor = 0;
  long resultTestGetData = 0;
  dword timeToWait = 5000; //in ms
}

MainTest()
{
  //save the bus context for later use
  a429Ch5Context = getBusNameContext ("A429Ch5");
  a429Ch6Context = getBusNameContext ("A429Ch6");
  
  TestJoinA429WordEvent_Any ();
}

testcase TestJoinA429WordEvent_Any ()
{
  a429word * myWord;
  dword index = 0;
  
  TestStepPass("Library: Test.can", "Testcase: TestJoinA429WordEvent_Any");
  
  TestStep ("Join Condition", "Create Join for LBL_075");
  //set the bus context to the correct hw bus
  setBusContext (a429Ch5Context);
  resultTestJoin = TestJoinA429WordEvent (LBL_075);
  if( resultTestJoin <= 0)
  {
    TestStepFail ("Join Condition", "result = %d, Failure on joining symbolic event: LBL_075", resultTestJoin);
  }
  else
  {
    TestStepPass ("Join Condition", "Joining symbolic event is ok");
  }
  
  TestStep ("Join Condition", "Create Join for LBL_012");
  //set the bus context to the correct hw bus

  setBusContext (a429Ch6Context);
  resultTestJoin = TestJoinA429WordEvent (LBL_012);
  if( resultTestJoin <= 0)
  {
    TestStepFail ("Join Condition", "result = %d, Failure on joining symbolic event: LBL_012", resultTestJoin);
  }
  else
  {
    TestStepPass ("Join Condition", "Joining symbolic event is ok");
  }
  
  // wait for any events that occur
  TestStep ("Call TFS function", "TestWaitForAnyJoinedEvent(timeout=%d)", timeToWait);
  resultTestWaitFor = TestWaitForAnyJoinedEvent (timeToWait);
  
  if (resultTestWaitFor > 0) // Resume due to event occurred
   {
       TestStepPass("Wait condition", "Waiting for any event is ok. Resume event number = %d", resultTestWaitFor);
      TestStepPass("Call TFS function", " TestGetWaitEventMsgData (index=%d)", resultTestWaitFor);
      
      // extract resume event's data
      resultTestGetData = TestGetWaitEventMsgData(resultTestWaitFor, myWord);
      if (0 != resultTestGetData)
      {
         TestStepFail("Data extraction", "resTestGetData = %d, Data access to data of event %d could not be executed!", resultTestGetData, resultTestWaitFor);
      }
      else
      {
         TestStepPass("Data extraction", "Data of event %d successfully extracted. label=%d", resultTestWaitFor, myWord.ID);
      }
   }
   else
   {
      TestStepFail("Wait condition", "resTestWaitFor = %d, Waiting for any of joined events failed!", resultTestWaitFor);
   }
}
```

## Availability

| Since Version |
|---|
