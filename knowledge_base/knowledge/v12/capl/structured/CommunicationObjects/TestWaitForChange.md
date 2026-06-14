# TestWaitForChange

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long TestWaitForChange(COValue value, dword timeoutMs)
```

## Description

Waits for the next change of a communication object value. This is equivalent to calling TestWaitForChangeCountGreater (value, value.GetChangeCount(), timeoutMs).

Note that only changes which occur while the function waits are considered. If you want to wait for changes which may occur earlier, or if you want to wait for several changes, use TestWaitForChangeFlag or TestWaitForChangeCountGreater.

## Return Values

-2: Resume due to constraint violation

## Example

```c
long ret;
consumedEventRef * anEvent;
anEvent = lookupConsumedEvent(path);
// ...
ret = testWaitForChange(anEvent, 200);
```

## Availability

| Since Version |
|---|
