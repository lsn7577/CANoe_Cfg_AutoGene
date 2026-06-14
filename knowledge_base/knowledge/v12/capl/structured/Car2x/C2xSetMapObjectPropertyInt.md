# C2xSetMapObjectPropertyInt

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSetMapObjectPropertyInt( long handle, char propertyName[], long propertyValue );
```

## Description

With this function it is possible to support all integer attributes by using their specific property name regardless of whether supported by the convenience layer or not.

As the property names can change, it is recommended to use the convenient functions like C2xSetMapObjectFillColor. These functions take the responsibility to set the correct property name by default.

## Return Values

0 if success, else the set went wrong

## Availability

| Since Version |
|---|
