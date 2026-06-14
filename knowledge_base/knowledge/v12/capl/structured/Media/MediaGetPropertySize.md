# MediaGetPropertySize

> Category: `Media` | Type: `function`

## Syntax

```c
long MediaGetPropertySize(dword objHandle, char propertyName[], dword& width, dword& height);
```

## Description

Retrieves a property whose value is a size, expressed as a width and height. Properties can be retrieved on an object specific basis for a media type object (e.g. returned by MediaGetMediaType).

## Return Values

0: The function succeeded.

## Availability

| Since Version |
|---|
