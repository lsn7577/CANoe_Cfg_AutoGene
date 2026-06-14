# J1939ILSetMessageProperty

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILSetMessageProperty( dbMessage msg, char propertyName[], long propertyValue); // form 1
```

## Description

This function sets the internal property of a message.

## Example

```c
if (J1939ILSetMessageProperty(TSC1, "MessageCounterToContinue", 12) < 0)
{
  write("Can’t set message property ‘MessageCounterToContinue‘");
}
```

## Availability

| Since Version |
|---|
