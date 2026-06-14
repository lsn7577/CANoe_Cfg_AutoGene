# TestWaitForUpdateFlag

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long TestWaitForUpdateFlag(COValue value, dword timeoutMs)
```

## Description

Waits for the update flag of a communication object value to be set. Each CO value has an update flag which is set when the value is updated and reset through an explicit call to valueEntity::ClearUpdateFlag or valueEntity::ResetValueState.

Use this function instead of TestWaitForUpdate if an undetermined number of updates may occur between a point where you reset the flag and a point where at least one update must have occurred.

## Return Values

-2: Resume due to constraint violation

## Example

```c
long ret;
consumedEventRef * anEvent;
anEvent = lookupConsumedEvent(path);
anEvent.ClearUpdateFlag();
// ...
ret = testWaitForUpdateFlag(anEvent, 200);
```

## Availability

| Since Version |
|---|
