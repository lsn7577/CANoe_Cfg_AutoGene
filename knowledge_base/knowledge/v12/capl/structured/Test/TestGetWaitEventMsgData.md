# TestGetWaitEventMsgData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitEventMsgData (message aMessage);
```

## Description

If a message event is the last event that triggers a wait instruction, the message content can be called up with the first function.The second function can only be used for "joined events". The number of the "joined event" (return value of "testJoin...") is here being used as an index.

## Return Values

0: Data access successful

## Example

```c
// add msg event to the current set of “joined events” and fill the msg data to message ‘eventMessage’
dword index = 0;
TestJoinMessageEvent(VehicleMotion);
// ... other join events
index = TestWaitForAnyJoinedEvent(2000);

TestGetWaitEventMsgData(index, eventMessage);
```

## Availability

| Since Version |
|---|
