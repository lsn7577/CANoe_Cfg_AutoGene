# TestValidateTesterAction

> Category: `Test` | Type: `function`

## Syntax

```c
long TestValidateTesterAction(char[] actionText, char[] heading, char[] callback, DWORD timeout, long resultOnAbort, Signal callbackTrigger); //form 1
```

## Description

Creates a popup window with the given tester instruction. The window closes automatically when the needed condition is fulfilled or after user cancel. The condition is checked every time when the given trigger occurs. The check of the condition must be implemented in the given CAPL callback. The window contains a field for entering a comment which is automatically adopted into the test report.The result of the command is reported.

The function is not allowed in CANoe standalone mode. Errors are reported as error in test system or fail in case of 2-valued verdict concept.

Form 5 is used with the functions TestCreateTesterAction and TestAddTriggerTesterAction to create complex tester actions with multiple triggers.

## Return Values

0: Timeout occurs.

## Example

```c
int CallbackSignal()
{
  if(@sysVarEngineStarted == 1)
    return 1;

  return 0;
}

testcase TCTesterAction()
{
  TestValidateTesterAction("This is the tester action text", "Tester action heading", "CallbackSignal", 10000, 3, SigSigned16);
}
```

## Availability

| Since Version |
|---|
