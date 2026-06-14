# TestJoinJ1939DTCEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinJ1939DTCEvent (dword sourceAddress, Message message, dword spn); // form 1
```

## Description

Completes the current set of joined events with the additional Diagnostic Trouble Code (DTC) event – transmitted with one of the J1939 diagnostic messages. This function does not wait.

The affected message (specified by the Parameter Group number pgn or the database object message) must be able to contain a DTC, so only this parameter groups are allowed: DM1, DM2, DM4, DM6, DM12, DM23, DM24, DM27, DM28, DM31, DM35 and DM41-DM54.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

-3: Join error

## Example

```c
testcase tcWaitForOneOfDTCs(dword sourceAddress)
{
  long eventIndex;
  dword sa = 0x1;

  //All DTCs are transmitted with the message DM12 (pgn = 0xFED4).
  dword pgnDM12 = 0xFED4;

  //DTC Condition 1: spn = 111, fmi = 12, oc to be ignored
  TestJoinJ1939DTCEvent (sourceAddress, pgnDM12, 111, 12, 0xFFFF);

  //DTC Condition 2: spn = 222, fmi to be ignored, oc = 5
  TestJoinJ1939DTCEvent (sourceAddress, pgnDM12, 222, 0xFFFF, 5);

  //DTC Condition 3: spn = 333, fmi and oc to be ignored
  TestJoinJ1939DTCEvent (sourceAddress, pgnDM12, 333, 0xFFFF, 0xFFFF);

  eventIndex = testWaitForAnyJoinedEvent(5000);
  switch (eventIndex)
  {

    case 1:
      testStepPass("Validation", "DTC with spn=111 and fmi=12 occurred");
      break;

    case 2:
      testStepPass("Validation", "DTC with spn=222 and oc=5 occurred");
      break;

    case 3:
      testStepPass("Validation", "DTC with spn=333 occurred");
      break;

    default:
      testStepFail("Validation", "Unexpected event or timeout (return code %d)", eventIndex);
      break;

  }
}
```

## Availability

| Since Version |
|---|
