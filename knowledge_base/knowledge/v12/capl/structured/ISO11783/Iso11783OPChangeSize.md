# Iso11783OPChangeSize

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPChangeSize( dword ecuHandle, dword objectID, dword width, dword height );
```

## Description

The function changes the size of an object. A Change Size command to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPChangeSize( 
 handle, 1200, 80, 40 );
```

## Availability

| Since Version |
|---|
