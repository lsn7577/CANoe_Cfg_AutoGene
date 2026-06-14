# Iso11783OPGetNumericValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPGetNumericValue( dword ecuHandle, dword objectID );
```

## Description

The function returns a numeric value of an object. The object must exist in the object pool and must support a numeric value.

## Return Values

Integer value of the object.
If a value of 0 is returned, you can check with the function Iso11783GetLastError if the function succeeded.

## Example

```c
LONG val;
val = Iso11783OPGetNumericValue( handle, 1000 );
```

## Availability

| Since Version |
|---|
