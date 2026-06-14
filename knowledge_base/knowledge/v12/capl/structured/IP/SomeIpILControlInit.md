# SomeIpILControlInit

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpILControlInit();
```

## Description

Initialization of SOME/IP IL.

Prevents the SOME/IP IL from starting automatically. If this function is used, the SOME/IP IL must then be started with the SomeIpILControlStart function.

This function may only be used in on preStart.

## Return Values

0: The function was successfully executed

## Example

```c
on preStart
{
  // prevent auto start
  SomeIpILControlInit();
}
```

## Availability

| Since Version |
|---|
