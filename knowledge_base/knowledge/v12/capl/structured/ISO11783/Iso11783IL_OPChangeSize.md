# Iso11783IL_OPChangeSize

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPChangeSize( dword objectID, dword width, dword height ); // form 1
```

## Description

The function changes the size of an object. A Change Size command to the Virtual Terminal.

## Example

```c
Iso11783IL_OPChangeSize( 
 1200, 80, 40 );
```

## Availability

| Since Version |
|---|
