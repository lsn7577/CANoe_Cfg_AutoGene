# SomeIpILControlWait

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpILControlWait();
```

## Description

Stops sending cyclic messages.

Application Endpoints and Provided Services are not deleted, Service Discovery continues to run. Messages continue to be received by SOME/IP IL and can be evaluated.

Use SomeIpILControlResume to send cyclic messages again.

## Return Values

0: The function was successfully executed

## Example

```c
on key 'w'
{
  // stop sending messages
  SomeIpILControlWait();
}
```

## Availability

| Since Version |
|---|
