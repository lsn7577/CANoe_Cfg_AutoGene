# on fctCalled

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on fctCalled <function>
```

## Description

The event procedure is called when a service function is called at a provider. At this time, the automatic answering feature has already set the out parameters and return value to their default values if it is configured.

## Example

```c
on fctCalled MirrorAdjustment[all,LeftMirror].Adjust
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
