# J1939GetEnvInt

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939GetEnvInt( char[] envVar, dword index );
```

## Description

This function gets the value of an environment variable.

## Return Values

value of the environment variable or 0 if it does not exist

## Example

```c
value = J1939GetEnvInt( "EvFrictionForce", 
 1 );
```

## Availability

| Since Version |
|---|
