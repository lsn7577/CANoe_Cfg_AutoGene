# TestWaitForA429Word

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForA429Word (dbA429Word aWord, dword aTimeout);
```

## Description

Wait for the occurrence of the specified word aWord. In case the ARINC word does not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless. If no specific ARINC word is given, the wait condition is resolved on any word.

If ARINC word events are delivered from different buses, the context has to be adjusted correctly (SetBusContext).

The function handles only incoming and error free ARINC words.

## Return Values

-2: Resume due to constraint violation

## Example

```c
//Example
//This example waits for the occurrence of two messages in correct order
variables
{
  dword a429Ch5Context = 0;
  dword a429Ch6Context = 0;
  long resultTestWait = 0;

  dword timeToWait = 5000; //in ms
}

MainTest()
{
  //save the bus context for later use
  a429Ch5Context = getBusNameContext ("A429Ch5");
  a429Ch6Context = getBusNameContext ("A429Ch6");
  
  TestWaitForA429Word_Two ();
}

testcase TestWaitForA429Word_Two()
{
  a429word * myWord;
  dword index = 0;
  
TestStepPass("Library: Test.can", "Testcase: TestWaitForA429Word_Two");

  TestStep ("Wait Condition", "Create Wait for LBL_075");
  
  setBusContext (a429Ch5Context);
  CheckWaitResult (testWaitForA429Word (LBL_075, timeToWait));
  
  TestStep ("Wait Condition", "Create Wait for LBL_012");
  setBusContext (a429Ch6Context);
  CheckWaitResult (testWaitForA429Word (LBL_012, timeToWait));
}

testfunction CheckWaitResult(long result)
{
  if( result < 0)
  {
    TestStepFail ("Wait Condition", "result = %d, Failure on joining symbolic event: LBL_075", result);
  }
  else if( result == 0)
  {
    TestStepFail ("Wait Condition", "result = %d, Failure on waiting symbolic event: LBL_075, event did not occur", result);
  }
  else
  {
    TestStepPass ("Wait Condition", "Awaited symbolic event occurred");
  }
}
```

## Availability

| Since Version |
|---|
