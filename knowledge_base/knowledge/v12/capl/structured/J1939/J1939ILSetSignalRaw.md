# J1939ILSetSignalRaw

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILSetSignalRaw(dbSignal signal, long value ); // form 1
```

## Description

Sets the signal to the specified raw value. The message of the signal is sent according the configured send type.

## Example

```c
on key 't'
{
 J1939ILSetSignalRaw( EEC1::EngSpeed, 12000 );
}
```

## Availability

| Since Version |
|---|
