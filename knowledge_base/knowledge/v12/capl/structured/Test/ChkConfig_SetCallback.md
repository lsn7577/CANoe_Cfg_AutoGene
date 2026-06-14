# ChkConfig_SetCallback

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkConfig_SetCallback(dword aCheckId, char [] CaplCallback);
check.SetCallback(char [] CaplCallback);
```

## Description

Sets a CAPL callback for the check. An already existing callback will be overwritten.This function can be used if the check itself has no syntax to create/start and to assign a callback.

## Return Values

0: successful

## Example

```c
void callback(dword id)
{
  // do something
}
testcase TC1()
{
  int checkId;

  checkId = ChkCreate_MsgOccurrenceCount(MsgA1, 3);

  testAddCondition(checkId);
  ChkConfig_SetCallback(checkId, "callback");
  ChkControl_Start(checkId);

  testWaitForTimeout(3000);

  ChkControl_Stop(checkId);
  testRemoveCondition(checkId);
}
```

## Availability

| Since Version |
|---|
