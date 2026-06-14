# Iso11783IL_PDDSetValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDSetValue( dbSignal signal, dword elementNumber, float value ); // form 1
```

## Description

Sets the value of a process variable.

## Example

```c
Iso11783IL_PDDSetValue( 0x200. 3, value );
Iso11783IL_PDDSetValue( 0x200. 4, value );
```

## Availability

| Since Version |
|---|
