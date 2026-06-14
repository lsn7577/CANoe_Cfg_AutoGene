# Iso11783PDDSetValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783PDDSetValue( dword ecuHandle, dbSignal signal, dword elementNumber, float alue );
```

## Description

Sets the value of a process variable.

## Return Values

error code

## Example

```c
Iso11783PDDSetValue( Sprayer, 0x200. 3, value );
Iso11783PDDSetValue( Sprayer, 0x200. 4, value );
```

## Availability

| Since Version |
|---|
