# Iso11783IL_SetMessageProperty

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_SetMessageProperty( dbMessage msg, char propertyName[], long propertyValue);
```

## Description

This function sets the internal property of a message.

## Return Values

0: Success (property has been set successfully)

## Example

```c
if (Iso11783IL_SetMessageProperty(TSC1, "MessageCounterToContinue", 12) < 0)
{
  write("Can’t set message property ‘MessageCounterToContinue‘");
}
```

## Availability

| Since Version |
|---|
