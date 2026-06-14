# Iso11783GetEnvDbl

> Category: `ISO11783` | Type: `function`

## Syntax

```c
double Iso11783GetEnvDbl( char envVar[], dword index );
```

## Description

This function gets the value of an environment variable.

## Return Values

Value of the environment variable or 0.0 if it does not exist

## Example

```c
value 
 = Iso11783GetEnvDbl( „EvFrictionForce“, 
 1 );
```

## Availability

| Since Version |
|---|
