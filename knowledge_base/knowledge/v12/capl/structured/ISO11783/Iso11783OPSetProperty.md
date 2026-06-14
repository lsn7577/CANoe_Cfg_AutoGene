# Iso11783OPSetProperty

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPSetProperty( dword ecuHandle, char propertyName[], long newValue );
```

## Description

The function sets a property of the Object Pool API, i.e. the supported Virtual Terminal version.

## Example

```c
Iso11783OPSetProperty( handle, "Version", 3 );
```

## Availability

| Since Version |
|---|
