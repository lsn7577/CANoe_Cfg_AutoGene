# Iso11783OPSetNumericValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPSetNumericValue( dword ecuHandle, dword objectID, long numericValue );
```

## Description

The function sets the numerical value of an object. The object must exist in the object pool and must support a numerical value. If the Object Pool API is active, a Change Numeric Value command is sent to the Virtual Terminal. This can be suppress with Bit 0 in options.

## Return Values

0 or error code

## Example

```c
Iso11783OPSetNumericValue( handle, 1000, 100 );
```

## Availability

| Since Version |
|---|
