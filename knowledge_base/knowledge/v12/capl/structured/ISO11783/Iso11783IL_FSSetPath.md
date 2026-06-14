# Iso11783IL_FSSetPath

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_FSSetPath( char path[] );
```

## Description

This function sets the root directory for the FS file functions of the interaction layer.

## Return Values

0: Function has been executed successfully

## Example

```c
Iso11783IL_FSSetPath( 
 "FSRoot" );
```

## Availability

| Since Version |
|---|
