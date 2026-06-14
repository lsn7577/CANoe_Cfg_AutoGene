# J1939GetEnvDbl

> Category: `J1939` | Type: `function`

## Syntax

```c
double J1939GetEnvDbl( char envVar[], dword index );
```

## Description

This function gets the value of an environment variable.

## Return Values

value of the environment variable or 0.0 if it does not exist

## Example

```c
value = J1939GetEnvDbl( „EvFrictionForce“, 1 );
```

## Availability

| Since Version |
|---|
