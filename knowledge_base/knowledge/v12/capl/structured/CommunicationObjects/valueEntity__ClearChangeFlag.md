# valueEntity::ClearChangeFlag

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
dword <value>::ClearChangeFlag()
```

## Description

Clears the change flag of the value. It will be set again when the value changes the next time. You can wait for the flag to be set with TestWaitForChangeFlag.

Using the change flag instead of waiting for a single change has the advantage that it doesn’t matter how many times the value is changed or in which order two values are changed.

## Return Values

—

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
