# Iso11783IL_OPChangeBackgroundColor

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPChangeBackgroundColor( dword objectID, dword color ); // form 1
```

## Description

This function changes the background color of an object. The Change Background Color command is sent to the Virtual Terminal.

## Return Values

0: Function has been executed successfully

## Example

```c
Iso11783IL_OPChangeBackgroundColor( 1200, 5 );
```

## Availability

| Since Version |
|---|
