# Iso11783SetEnvDbl

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783SetEnvDbl( char envVar[], dword index, float value );
```

## Description

This function sets the value of an environment variable.

## Return Values

0 on success or error code

## Example

```c
Iso11783SetEnvDbl( "EvFrictionForce", 
 1, 33.12 );
```

## Availability

| Since Version |
|---|
