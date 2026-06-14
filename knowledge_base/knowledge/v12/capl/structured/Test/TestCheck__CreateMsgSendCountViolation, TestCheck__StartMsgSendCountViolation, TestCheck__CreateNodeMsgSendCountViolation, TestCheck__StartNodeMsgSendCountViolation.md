# TestCheck::CreateMsgSendCountViolation, TestCheck::StartMsgSendCountViolation, TestCheck::CreateNodeMsgSendCountViolation, TestCheck::StartNodeMsgSendCountViolation

> Category: `Test` | Type: `function`

## Syntax

```c
TestCheck::CreateMsgSendCountViolation, TestCheck::StartMsgSendCountViolation, TestCheck::CreateNodeMsgSendCountViolation, TestCheck::StartNodeMsgSendCountViolation(slotID);
```

## Description

Monitors the bus and reports if at least aMinCount and at most aMaxCountfor each of the defined messages occurred within a specified time interval aInterval.

If a DB node is used as reference, then all its Tx frames are observed.

For FlexRay only valid data frames and PDUs are recognized as communication, Null Frames and Erroneous frames are ignored.

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

  // Frames that are sent by node Controller_Node_1:
  FrFrame MsgChannel1.Sync_Message_1_Ch_A      frame2;
  FrFrame MsgChannel1.Sync_Message_1_Ch_B      frame2b;
  FrFrame MsgChannel1.TimeSync_Message_1_Ch_A  frame15;

  const dword cFrFlagTT      = 0x00;
  const dword cFrFlagET      = 0x10;
  const dword cFrFlagStop    = 0x80;
}

testcase GoodCheckNodeMsgSendCountViolation_1 ()
{
  TestCheck c;
  dword cMinCount = 1;
  dword cMaxCount = 0; // ignore
  dword cInterval = 320; // [ms]

  // Assure check to succeed:
  frame2.FR_Flags = cFrFlagTT; // start sending the frame
  
  FRUpdateStatFrame(frame2);
  frame2b.FR_Flags = cFrFlagTT; // start sending the frame
  
  FRUpdateStatFrame(frame2b);
  frame15.FR_Flags = cFrFlagTT; // start sending the frame
  
  FRUpdateStatFrame(frame15);
  TestWaitForTimeout(330);

  c = TestCheck::CreateNodeMsgSendCountViolation( Controller_Node_1, cMinCount, cMaxCount, cInterval );

  TestAddCondition(c);

  c.start();
  TestWaitForTimeout(cTesttime);

  TestRemoveCondition(c);
}
```

## Availability

| Since Version |
|---|
