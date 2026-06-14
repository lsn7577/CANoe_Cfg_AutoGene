# AREthILControlWait

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthILControlWait();
```

## Description

Stops sending cyclic messages.

Application Endpoints and Provided Services are not deleted, Service Discovery continues to run. Messages continue to be received by AUTOSAR Eth IL and can be evaluated.

Use AREthILControlResume to send cyclic messages again.

## Return Values

0: The function was successfully executed

## Example

```c
on key 'w'
{
  // stop sending messages
  AREthILControlWait();
}
```

## Availability

| Since Version |
|---|
