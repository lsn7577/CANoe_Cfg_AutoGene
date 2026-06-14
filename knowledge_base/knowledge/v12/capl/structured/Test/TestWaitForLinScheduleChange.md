# TestWaitForLinScheduleChange

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForLinScheduleChange(dword aTimeout); // form 1
```

## Description

Waits until the LIN scheduler reaches the specified table and slot index. If no indices are specified, the function will resume on the next change of the current table or slot index.

Should the event not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

## Example

```c
testcase tc_WaitForLinScheduleChange()

{
  long result;

  // Waits until the scheduler reaches slot 1 of schedule table 1
  result = TestWaitForLinScheduleChange(1, 1, 5000);

  if (result != 1)
  {
    testStepFail("TestWaitForLinScheduleChange failed!");
    testCaseFail();
  }
}
```

## Availability

| Since Version |
|---|
