# on fctReturned

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on fctReturned <function>
```

## Description

The event procedure is called at the consumer when a service function answer is returned to the consumer.

## Example

```c
on fctReturned MirrorAdjustment[CANoe,LeftMirror].Adjust
{
  write("Function result is %d", this.Result);
}
```

## Availability

| Since Version |
|---|

## Selectors

| callContext | ../Objects/CAPLfunctionCallContext.htm |
|---|---|
