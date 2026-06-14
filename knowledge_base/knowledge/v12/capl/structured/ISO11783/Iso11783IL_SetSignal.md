# Iso11783IL_SetSignal

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_SetSignal( dbSignal signal, double value );
```

## Description

Sets the signal to the specified physical value. The message of the signal is sent according the configured send type.

## Example

```c
on key 't'
{
 Iso11783IL_SetSignal( EEC1::EngSpeed, 1200.0 );
}
```

## Availability

| Since Version |
|---|
