# J1939ILSetSignal

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILSetSignal(dbSignal signal, double value ); // form 1
```

## Description

Sets the signal to the specified physical value. The message of the signal is sent according the configured send type.

## Example

```c
on key 't'
{
 J1939ILSetSignal( EEC1::EngSpeed, 1200.0 );
}
```

## Availability

| Since Version |
|---|
