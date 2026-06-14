# diagCheckValidNegResCode

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagCheckValidNegResCode( diagRequest obj, dword negResCode);
```

## Description

The functions return 1 if the given negative response code is defined for the object. It returns 0 if the code is not valid, and <0 for an error.

In the one-argument form, the response object has to be a negative response.

## Return Values

1: Code is defined for the object in the CDD.

## Availability

| Since Version |
|---|
