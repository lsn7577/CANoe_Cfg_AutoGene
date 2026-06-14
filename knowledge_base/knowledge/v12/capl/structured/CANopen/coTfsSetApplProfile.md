# coTfsSetApplProfile

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSetApplProfile( dword profile );
```

## Description

The function enables the support of an application profile. The function has to be called before any test functions are executed.

## Return Values

Error code

## Example

```c
coTfsSetApplProfile(447);

//...

coTfsSetApplProfile(301); // set back to default
```
