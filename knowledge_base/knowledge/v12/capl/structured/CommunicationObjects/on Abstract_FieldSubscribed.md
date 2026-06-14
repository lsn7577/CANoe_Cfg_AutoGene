# on Abstract_FieldSubscribed

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on Abstract_FieldSubscribed <Field>
```

## Description

The event procedure is called at the provider when a field is subscribed by a consumer and abstract binding is used.

## Example

```c
on Abstract_FieldSubscribed MirrorAdjustment[LeftMirror].CurrentPosition
{
  write("Field subscribed by %s", this.consumer.Name);
}
```

## Availability

| Since Version |
|---|

## Selectors

| fieldConsumerRef * | ../Objects/CAPLfunctionFieldConsumerRef.htm |
|---|---|
