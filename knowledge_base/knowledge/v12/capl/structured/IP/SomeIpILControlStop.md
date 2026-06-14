# SomeIpILControlStop

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpILControlStop();
```

## Description

Stops the SOME/IP IL.

Disables sending and receiving SOME/IP messages and Service Discovery. Application-Endpoints and Provided Services will be closed.

The SOME/IP IL can be started again using the SomeIpILControlStart function.

## Return Values

0: The function was successfully executed

## Example

```c
on key '2 '
{
  // stop IL manually
  SomeIpILControlStop();
}
```

## Availability

| Since Version |
|---|
