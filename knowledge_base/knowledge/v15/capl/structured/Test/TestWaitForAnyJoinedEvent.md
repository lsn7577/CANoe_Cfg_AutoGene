# TestWaitForAnyJoinedEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForAnyJoinedEvent(dword aTimeout);
```

## Description

Waits for the current set of "joined events." Each individual of these events can resolve the wait state.

Should none of the events occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

## Parameters

| Name | Description |
|---|---|
| aTimeout | Maximum time that should be waited [ms](Transmission of 0: no timeout controlling) |

## Example

```c
variables
{
  long EventHandle1, EventHandle2, lReturn;
  int64 mEventTime;
  long Res;
}

MainTest()
{
  _WaitForAnyEvent();
}

on errorFrame
{
  Res = TestSupplyTextEvent("ErrorFrame occurred!");
}


testcase _WaitForAnyEvent()
{
  TestCaseTitle("Demo","WaitForAnyJoinedEvents");

  EventHandle1 = testJoinSysVarEvent(sysvar::Sysvar1);
  EventHandle2 = TestJoinTextEvent("ErrorFrame occurred!");

  lReturn = TestWaitForAnyJoinedEvent (5000);


  if (lReturn > 0)
  {
    if (lReturn == EventHandle1)
    {
      Res = testGetJoinedEventOccured(lReturn, mEventTime);
      write("mEventTime = %I64d ; Res = %ld ; lReturn = %ld",mEventTime,Res,lReturn);
    }
    if (lReturn == EventHandle2)
    {
      Res = testGetJoinedEventOccured(lReturn, mEventTime);
      write("mEventTime = %I64d ; Res = %ld ; lReturn = %ld",mEventTime,Res,lReturn);
    }
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
