# diagStartAuth, diagStartAuthGeneric, _Diag_AuthResult

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagStartAuth(char ecuQualifier[], char jobQualifier[]); // form 1
```

## Description

Starts the diagnostics authentication process. The result is indicated to the callback function _Diag_AuthResult.

## Return Values

0 on success otherwise error code

## Example

```c
on key 'a'
{
  result = diagStartAuth("Ecu", "Developer");
  write("Start 'diagStartAuth' for %s with result = %ld", gEcu, result);
}

void _Diag_AuthResult(long result)
{
  write("On '_Diag_AuthResult' for %s with result = %d", gEcu, result);
}
```

## Availability

| Since Version |
|---|
