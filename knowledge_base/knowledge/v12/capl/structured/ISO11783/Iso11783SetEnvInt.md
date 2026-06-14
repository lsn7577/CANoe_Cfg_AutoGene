# Iso11783SetEnvInt

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783SetEnvInt( char envVar[], dword index, dword value );
```

## Description

This function sets the value of an environment variable.

## Return Values

0 on success or error code

## Example

```c
Iso11783SetEnvInt( „EvFrictionForce“, 
 1, 3 );
```

## Availability

| Since Version |
|---|
