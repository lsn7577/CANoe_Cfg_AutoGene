# Iso11783IL_OPShowObject

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPShowObject( dword objectID, dword show ); // form 1
```

## Description

The function shows or hides an object. The Show Object command is sent to the Virtual Terminal.

## Example

```c
Iso11783IL_OPShowObject( 
 1200, 1 );
```

## Availability

| Since Version |
|---|
