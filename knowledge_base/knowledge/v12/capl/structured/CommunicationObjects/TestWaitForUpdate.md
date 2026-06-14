# TestWaitForUpdate

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long TestWaitForUpdate(COValue value, dword timeoutMs)
```

## Description

Waits for the next update of a communication object value. This is equivalent to calling TestWaitForUpdateCountGreater (value, value.GetUpdateCount(), timeoutMs).

Note that only updates which occur while the function waits are considered. If you want to wait for updates which may occur earlier, or if you want to wait for several updates, use TestWaitForUpdateFlag or TestWaitForUpdateCountGreater.

## Return Values

-2: Resume due to constraint violation

## Example

```c
long ret;
consumedEventRef * anEvent;
anEvent = lookupConsumedEvent(path);
// ...
ret = testWaitForUpdate(anEvent, 200);
```

## Availability

| Since Version |
|---|
