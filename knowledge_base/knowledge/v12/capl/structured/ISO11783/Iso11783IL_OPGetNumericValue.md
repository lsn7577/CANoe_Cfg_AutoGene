# Iso11783IL_OPGetNumericValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPGetNumericValue( dword objectID ); // form 1
```

## Description

The function returns a numeric value of an object. The object must exist in the object pool and must support a numeric value.

## Return Values

integer value of the object
If a value of 0 is returned, you can check with the function Iso11783IL_GetLastError if the function succeeded.

## Example

```c
LONG val;
val = Iso11783IL_OPGetNumericValue( 1000 );
```

## Availability

| Since Version |
|---|
