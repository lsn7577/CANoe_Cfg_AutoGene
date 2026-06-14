# Iso11783IL_OPGetProperty

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPGetProperty( char propertyName[] ); // form 1
```

## Description

Returns a property of the Object Pool API, e.g. the supported VT version.

## Return Values

>= 0: Value

## Example

```c
LONG version;
version = Iso11783IL_OPGetProperty( "Version" );
```

## Availability

| Since Version |
|---|
