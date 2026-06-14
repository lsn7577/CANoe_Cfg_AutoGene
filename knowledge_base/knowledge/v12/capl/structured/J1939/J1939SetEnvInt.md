# J1939SetEnvInt

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939SetEnvInt( char envVar[], dword index, dword value );
```

## Description

This function sets the value of an environment variable.

## Return Values

0 on success or error code

## Example

```c
J1939SetEnvInt( „EvFrictionForce“, 1, 3 );
```

## Availability

| Since Version |
|---|
