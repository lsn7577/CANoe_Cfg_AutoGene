# TestJoinMessageEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinMessageEvent (dbMessage aMessage)
```

## Description

Completes the current set of "joined events" with the transmitted event. This function does not wait.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

-3: Join error

## Example

```c
// add msg event to the current set of “joined events” and fill the msg data to message ‘eventMessage’
dword index = 0;
TestJoinMessageEvent(VehicleMotion);
// ... other join events
TestJoinEnvVarEvent(MyEnvVar);
TestJoinSignalInRange(Velocity, 80, 100);
TestJoinTextEvent("ErrorFrame occurred!");

index = TestWaitForAnyJoinedEvent(2000);

TestGetWaitEventMsgData(index, eventMessage);
```

## Availability

| Since Version |
|---|
