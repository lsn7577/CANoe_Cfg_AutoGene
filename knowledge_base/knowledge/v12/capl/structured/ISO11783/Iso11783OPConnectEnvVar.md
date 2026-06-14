# Iso11783OPConnectEnvVar

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPConnectEnvVar( dword ecuHandle, char envVarName[], dword objectId );
```

## Description

Connects an object (variable, value or string) from the object pool to an environment variable.

If an object is changed, the new value is put the environment variable. And vice versa, if the value of an environment variable is changed, the new value is also written to the connected object. Additionally a Change String or Change Numeric Value command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPConnectEnvVar( handle, "EnvSprayer_AppRate", 1040 );
```

## Availability

| Since Version |
|---|
