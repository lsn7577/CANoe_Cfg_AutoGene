# Iso11783IL_OPSetNumericValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPSetNumericValue( dword objectID, long numericValue ); // form 1
```

## Description

The function sets the numerical value of an object. The object must exist in the object pool and must support a numerical value. If the Object Pool API is active, a Change Numeric Value command is sent to the Virtual Terminal. This can be suppress with Bit 0 in options.

## Example

```c
Iso11783IL_OPSetNumericValue( 1000, 100 );
```

## Availability

| Since Version |
|---|
