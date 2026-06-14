# Iso11783IL_OPChangeChildPosition

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPChangeChildPosition( dword parentID, dword objectID, long x, long y ); // form 1
```

## Description

The function changes the absolute position of an object inside its parent object. A Change Child Position command is sent to the Virtual Terminal.

## Return Values

0: Function has been executed successfully

## Example

```c
Iso11783IL_OPChangeChildPosition( 1000, 1200, 10, 10 );
```

## Availability

| Since Version |
|---|
