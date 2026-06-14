# on fctCalling

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on fctCalling <function>
```

## Description

The event procedure is called when a service function is about to be called at a provider. At this time, the automatic answering feature has not yet set out parameters or delay, so you can still use the ParamDefaults or DefaultResult values to configure it.

## Example

```c
on fctCalling MirrorAdjustment[all,LeftMirror].Adjust
{
  if (abs(this.deltaX) > MAX_X || abs(this.deltaY) > MAX_Y)
  {
    $MirrorAdjustment.providerSide[all,LeftMirror].Adjust.DefaultResult = Mirrors::AdjustResult::OutOfRange;
  }
  else
  {
    $MirrorAdjustment.providerSide[all,LeftMirror].Adjust.DefaultResult = Mirrors::AdjustResult::OK;
  }
}
```

## Availability

| Since Version |
|---|

## Selectors

| callContext | ../Objects/CAPLfunctionCallContext.htm |
|---|---|
