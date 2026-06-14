# AREthILControlStart

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthILControlStart();
```

## Description

Starts AUTOSAR Eth IL.

Enabled sending and receiving SOME/IP messages and Service Discovery. After the start of AUTOSAR Eth IL, all Application Endpoints and the Provided Services must be created.

AUTOSAR Eth IL can be stopped using the AREthILControlStop function.

## Return Values

0: The function was successfully executed

## Example

```c
on key '1'
{
  // start IL manually
  AREthILControlStart();

  // add application endpoints and provided services here
}
```

## Availability

| Since Version |
|---|
