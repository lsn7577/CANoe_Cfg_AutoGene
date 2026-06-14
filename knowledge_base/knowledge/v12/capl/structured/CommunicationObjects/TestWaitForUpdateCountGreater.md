# TestWaitForUpdateCountGreater

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long TestWaitForUpdateCountGreater(COValue value, qword count, dword timeoutMs)
```

## Description

Waits for the update counter of a communication object value to reach a certain value. Each CO value contains an update counter which is reset to 0 at measurement start and with explicit calls to valueEntity::ResetValueState. You can read out the counter with valueEntity::GetUpdateCount.

## Return Values

-2: Resume due to constraint violation

## Example

```c
long ret;
consumedEventRef * anEvent;
anEvent = lookupConsumedEvent(path);
// ...
ret = testWaitForUpdateCountGreater(anEvent, anEvent.GetUpdateCount() + 3, 200);
```

## Availability

| Since Version |
|---|
