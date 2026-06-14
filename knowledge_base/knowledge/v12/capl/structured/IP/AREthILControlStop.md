# AREthILControlStop

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthILControlStop();
```

## Description

Stops the AUTOSAR Eth IL.

Disables sending and receiving SOME/IP messages and Service Discovery. Application-Endpoints and Provided Services will be closed.

The AUTOSAR Eth IL can be started again using the AREthILControlStart function.

## Return Values

0: The function was successfully executed

## Example

```c
on key '2 '
{
  // stop IL manually
  AREthILControlStop();
}
```

## Availability

| Since Version |
|---|
