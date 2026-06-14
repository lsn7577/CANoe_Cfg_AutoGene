# Iso11783OPChangeLineAttribute

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPChangeLineAttribute( dword ecuHandle, dword objectID, dword color, dword width, dword art );
```

## Description

The function changes the properties of a line attribute object. A Change Line Attribute command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPChangeLineAttributeibute( handle, 1100, 10, 3, 0xaa );
```

## Availability

| Since Version |
|---|
