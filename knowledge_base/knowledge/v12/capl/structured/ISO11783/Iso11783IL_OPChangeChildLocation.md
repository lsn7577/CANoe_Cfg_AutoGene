# Iso11783IL_OPChangeChildLocation

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPChangeChildLocation( dword parentID, dword objectID, long dx, long dy ); // form 1
```

## Description

The function moves an object. The object is moved relative inside the parent object. A Change Child Location command is sent to the Virtual Terminal.

## Return Values

0: Function has been executed successfully

## Example

```c
// move object 5 pixels to the right
Iso11783IL_OPChangeChildLocation( 1000, 
 1200, 5, 0 );
```

## Availability

| Since Version |
|---|
