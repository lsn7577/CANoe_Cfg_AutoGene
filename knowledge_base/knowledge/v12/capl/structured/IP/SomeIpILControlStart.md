# SomeIpILControlStart

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpILControlStart();
```

## Description

Starts SOME/IP IL.

Enabled sending and receiving SOME/IP messages and Service Discovery. After the start of SOME/IP IL, all Application Endpoints and the Provided Services must be created.

SOME/IP IL can be stopped using the SomeIpILControlStop function.

## Return Values

0: The function was successfully executed

## Example

```c
on key '1'
{
  // start IL manually
  SomeIpILControlStart();

  // add application endpoints and provided services here
}
```

## Availability

| Since Version |
|---|
