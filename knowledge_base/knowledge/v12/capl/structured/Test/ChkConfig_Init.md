# ChkConfig_Init

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkConfig_Init (char aRole[]); // form 1: deprecated
```

## Description

Initializes TSL to be used subsequently.

If the function is used, then it is recommended to perform the initialization once during preStart section of the CAPL program.

The tester role (form 1) has no longer an effect.

## Return Values

-1: error

## Example

```c
// test is executed in the role of a developer
on preStart
{
   ChkConfig_Init();
}
```

## Availability

| Since Version |
|---|
