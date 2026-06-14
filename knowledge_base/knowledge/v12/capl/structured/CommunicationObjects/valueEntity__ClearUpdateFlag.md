# valueEntity::ClearUpdateFlag

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
dword <value>::ClearUpdateFlag()
```

## Description

Clears the update flag of the value. It will be set again when the value is updated the next time. You can wait for the flag to be set with TestWaitForUpdateFlag.

Using the update flag instead of waiting for a single update has the advantage that it doesn’t matter how many times the value is updated or in which order two values are updated.

## Return Values

—

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
