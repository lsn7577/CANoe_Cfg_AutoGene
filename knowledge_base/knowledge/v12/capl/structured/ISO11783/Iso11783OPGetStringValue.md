# Iso11783OPGetStringValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPGetStringValue( dword ecuHandle, dword objectID, dword bufferSize, char buffer[] );
```

## Description

The function copies a string value of an object in the object pool into a buffer. The object must exist in the object pool and support a string value.

## Example

```c
char buffer[100];
Iso11783OPGetStringValue( handle, 1000, elCount(buffer), buffer );
```

## Availability

| Since Version |
|---|
