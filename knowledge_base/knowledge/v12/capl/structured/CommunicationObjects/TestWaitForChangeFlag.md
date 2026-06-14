# TestWaitForChangeFlag

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long TestWaitForChangeFlag(COValue value, dword timeoutMs)
```

## Description

Waits for the change flag of a communication object value to be set. Each CO value has a change flag which is set when the value changes and reset through an explicit call to valueEntity::ClearChangeFlag or valueEntity::ResetValueState.

Use this function instead of TestWaitForChange if an undetermined number of changes may occur between a point where you reset the flag and a point where at least one change must have occurred.

## Return Values

-2: Resume due to constraint violation

## Example

```c
long ret;
consumedEventRef * anEvent;
anEvent = lookupConsumedEvent(path);
anEvent.ClearChangeFlag();
// ...
ret = testWaitForChangeFlag(anEvent, 200);
```

## Availability

| Since Version |
|---|
