# valueEntity::GetValueState

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
dword <value>::GetValueState()
```

## Description

Returns the state of the value, which tells in particular whether it has already been updated once since the last call to valueEntity::ResetValueState.

## Return Values

State of the value:

## Example

```c
long ret;
consumedEventRef * anEvent;
anEvent = lookupConsumedEvent(path);
if (anEvent.GetValueState() != 3) // not yet received
{
  anEvent.ClearUpdateFlag();
  ret = testWaitForUpdateFlag(anEvent, 200);
  // ...
}
```

## Availability

| Since Version |
|---|
