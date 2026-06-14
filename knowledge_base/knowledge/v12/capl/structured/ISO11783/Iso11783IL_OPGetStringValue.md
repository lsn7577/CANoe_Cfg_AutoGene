# Iso11783IL_OPGetStringValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPGetStringValue( dword objectID, dword bufferSize, char buffer[] ); // form 1
```

## Description

The function copies a string value of an object in the object pool into a buffer. The object must exist in the object pool and support a string value.

## Example

```c
char buffer[100];
Iso11783IL_OPGetStringValue( 1000, elCount(buffer), buffer );
```

## Availability

| Since Version |
|---|
