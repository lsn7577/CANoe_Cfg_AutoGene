# on fctReturning

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on fctReturning <function>
```

## Description

The event procedure is called when a service function is about to return its answer at a provider. At this time, the automatic answering feature has already set the out parameters and return value to their default values if it is configured and the default answer time has elapsed.

The handler is particularly useful if the answer time is determined by another component.

## Example

```c
on fctReturning MirrorAdjustment[all,LeftMirror].Adjust
{
  if (abs(this.deltaX) > MAX_X || abs(this.deltaY) > MAX_Y)
  {
    this.Result = Mirrors::AdjustResult::OutOfRange;
  }
  else
  {
    this.Result = Mirrors::AdjustResult::OK;
  }
}
```

## Availability

| Since Version |
|---|

## Selectors

| callContext | ../Objects/CAPLfunctionCallContext.htm |
|---|---|
