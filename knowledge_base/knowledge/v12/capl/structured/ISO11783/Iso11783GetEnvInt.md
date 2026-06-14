# Iso11783GetEnvInt

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783GetEnvInt( char[] envVar, dword index );
```

## Description

This function gets the value of an environment variable.

## Return Values

Value of the environment variable or 0 if it does not exist

## Example

```c
value = Iso11783GetEnvInt( "EvFrictionForce", 
 1 );
```

## Availability

| Since Version |
|---|
