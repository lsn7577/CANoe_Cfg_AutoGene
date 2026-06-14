# Iso11783IL_SetSignalRaw

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_SetSignalRaw( dbSignal signal, long value );
```

## Description

Sets the signal to the specified raw value. The message of the signal is sent according the configured send type.

## Example

```c
on key 't'
{
 Iso11783IL_SetSignalRaw( EEC1::EngSpeed, 12000 );
}
```

## Availability

| Since Version |
|---|
