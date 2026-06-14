# TestCheck::CreateFlexRayFrameErrorOccurrenceCount, TestCheck::StartFlexRayFrameErrorOccurrenceCount, TestCheck::CreateNodeFlexRayFrameErrorsOccurrenceCount, TestCheck::StartNodeFlexRayFrameErrorsOccurrenceCount

> Category: `Test` | Type: `function`

## Syntax

```c
TestCheck::CreateFlexRayFrameErrorOccurrenceCount, TestCheck::StartFlexRayFrameErrorOccurrenceCount, TestCheck::CreateNodeFlexRayFrameErrorsOccurrenceCount, TestCheck::StartNodeFlexRayFrameErrorsOccurrenceCount(slotID);
```

## Description

Checks the absence of erroneous frames for the specified frame/slot on the bus. An event is created if more than aMaxCount of the specified erroneous frames were sent.

If a DB node is used as reference, then all its Tx frames are observed.

Since CANoe version 8.2 SP3 the numerical functions allow to define a wildcard event by setting slotID = -1, cycleOffs = 0, cycleRep = 1 in order to check for the absence of any FlexRay Erroneous Frame.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Parameters

| Name | Description |
|---|---|
| slotID | This number designates a specific FlexRay slot. |

## Example

```c
variables
{
  const dword cTesttime = 640; // [ms] per check

  FrFrame MsgChannel1.(10,0,2) frame10 = { FR_Flags = 0, FR_ChannelMask = 1, FR_PayloadLength = 2 };

  const dword cFrFlagTT      = 0x00;
  const dword cFrFlagET      = 0x10;
  const dword cFrFlagStop    = 0x80;
}

testcase GoodCheckFlexRayFrameErrorOccurrenceCount_1 ()
{
  TestCheck c;
  long cMaxCount = 0;

  // Assure check to succeed:
  frame10.FR_Flags = cFrFlagTT; // start sending the frame
  FRUpdateStatFrame(frame10);
  TestWaitForTimeout(12);

  c = TestCheck::CreateFlexRayFrameErrorOccurrenceCount( frame10.FR_SlotID, frame10.FR_CycleOffset, frame10.FR_CycleRepetition, frame10.FR_ChannelMask, cMaxCount);

  TestAddCondition(c);

  c.start();
  TestWaitForTimeout(cTesttime);

  TestRemoveCondition(c);
}
```

## Availability

| Since Version |
|---|
