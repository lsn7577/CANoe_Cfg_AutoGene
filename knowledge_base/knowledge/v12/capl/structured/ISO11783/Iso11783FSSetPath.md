# Iso11783FSSetPath

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783FSSetPath( char path[] );
```

## Description

This function sets the root directory for the FS file functions of the node layer.

## Return Values

0 or error code

## Example

```c
Iso11783FSSetPath( 
 "FSRoot" );
```

## Availability

| Since Version |
|---|
