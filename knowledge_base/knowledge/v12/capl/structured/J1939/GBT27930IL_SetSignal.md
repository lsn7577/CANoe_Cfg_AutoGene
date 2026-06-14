# GBT27930IL_SetSignal

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_SetSignal(dbSignal signal, double value ); // form 1
```

## Description

Sets the signal to the specified physical value. The message of the signal is sent according the configured send type.

## Example

```c
on key 't'
{
 GBT27930IL_SetSignal( EEC1::EngSpeed, 1200.0 );
}
```

## Availability

| Since Version |
|---|
