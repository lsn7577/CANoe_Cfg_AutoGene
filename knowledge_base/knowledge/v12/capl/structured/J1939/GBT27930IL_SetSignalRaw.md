# GBT27930IL_SetSignalRaw

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_SetSignalRaw(dbSignal signal, long value ); // form 1
```

## Description

Sets the signal to the specified raw value. The message of the signal is sent according the configured send type.

## Example

```c
on key 't'
{
 GBT27930IL_SetSignalRaw( EEC1::EngSpeed, 12000 );
}
```

## Availability

| Since Version |
|---|
