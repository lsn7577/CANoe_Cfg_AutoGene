# TestWaitForLinBitStreamStatus

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForLinBitStreamStatus(dword awaitedStatus, dword timeout); // form 1
```

## Description

Waits until the sending of a LIN bit stream is started or stopped. The function will resume immediately if the transmission already has the awaited status.

Should the event not occur before the expiration of the time timeout, the wait condition is resolved nevertheless.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

## Example

```c
testcase tc_TestWaitForLinBitStreamStatus()
{
  long  result;

  // Wait for a maximum time of 100ms for the bit stream to start sending
  result = TestWaitForLinBitStreamStatus(1, 100);

  if(result != 1)
  {
    testStepFail("The sending of the bit stream didn't start within 100ms!");
    testCaseFail();
  }
}
```

## Availability

| Since Version |
|---|
