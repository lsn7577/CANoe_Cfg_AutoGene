# Iso11783OPGetProperty

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPGetProperty( dword ecuHandle, char propertyName[] );
```

## Description

Returns a property of the Object Pool API, e.g. the supported VT version.

## Example

```c
LONG version;
version = Iso11783OPGetProperty( handle, "Version" );
```

## Availability

| Since Version |
|---|
