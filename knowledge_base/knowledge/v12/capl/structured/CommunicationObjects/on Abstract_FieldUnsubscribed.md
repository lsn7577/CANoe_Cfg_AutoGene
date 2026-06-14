# on Abstract_FieldUnsubscribed

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on Abstract_FieldUnsubscribed <Field>
```

## Description

The event procedure is called at the provider when a field is unsubscribed by a consumer and abstract binding is used.

## Example

```c
on Abstract_FieldUnsubscribed MirrorAdjustment[LeftMirror].CurrentPosition
{
  write("Field unsubscribed by %s", this.consumer.Name);
}
```

## Availability

| Since Version |
|---|

## Selectors

| fieldConsumerRef * | ../Objects/CAPLfunctionFieldConsumerRef.htm |
|---|---|
