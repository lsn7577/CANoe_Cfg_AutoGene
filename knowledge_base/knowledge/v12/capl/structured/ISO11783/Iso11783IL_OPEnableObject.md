# Iso11783IL_OPEnableObject

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPEnableObject( dword objectID, dword enable ); // form 1
```

## Description

The function activates or deactivates an input object. A Enable Object command is sent to the Virtual Terminal.

## Example

```c
Iso11783IL_OPEnableObject( 
 1200, 1 );
```

## Availability

| Since Version |
|---|
