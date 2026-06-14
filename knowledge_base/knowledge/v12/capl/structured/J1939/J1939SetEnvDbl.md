# J1939SetEnvDbl

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939SetEnvDbl( char envVar[], dword index, float value );
```

## Description

This function sets the value of an environment variable.

## Return Values

0 on success or error code

## Example

```c
J1939SetEnvDbl( "EvFrictionForce", 
 1, 33.12 );
```

## Availability

| Since Version |
|---|
