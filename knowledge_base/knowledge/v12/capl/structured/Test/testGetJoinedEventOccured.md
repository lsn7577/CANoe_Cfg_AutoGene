# testGetJoinedEventOccured

> Category: `Test` | Type: `function`

## Syntax

```c
long testGetJoinedEventOccured(dword index, int64& occurrenceTime);
```

## Description

Retrieves the occurrence and the occurrence time of a joined event.

## Return Values

0: Event not occurred

## Example

```c
MainTest()
{
  WaitForAllEvents();
}

on errorFrame
{
  TestSupplyTextEvent("ErrorFrame occurred!");
}

testcase WaitForAllEvents()
{
  const dword waitDuration = 5000; // [ms]
  long  eventHandle1, eventHandle2;
  int64 eventTime1  , eventTime2  ;
  long  res;

  TestCaseTitle("Demo", "WaitForAllEvents");

  eventHandle1 = testJoinSysVarEvent(sysvar::Sysvar1);
  eventHandle2 = TestJoinTextEvent("ErrorFrame occurred!");
  res = TestWaitForAllJoinedEvents(waitDuration);

  if (res > 0) // all events ocurred, last one is stored in res
  {
    write("All expected events occured");
  }
  else
  {
    write("Timeout after %d ms: Not all expected events occured", waitDuration);
  }

  if (testGetJoinedEventOccured(eventHandle1, eventTime1) == 1)
  {
    write("SysVar1 changed at %I64d", eventTime1);
  }
  else
  {
    write("SysVar1 unchanged");
  }

  if (testGetJoinedEventOccured(eventHandle2, eventTime2) == 1)
  {
    write("Errorframe occured at %I64d", eventTime2);
  }
  else
  {
    write("No Errorframe");
  }
}
```

## Availability

| Since Version |
|---|
