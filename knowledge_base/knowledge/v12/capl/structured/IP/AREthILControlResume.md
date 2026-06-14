# AREthILControlResume

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthILControlResume();
```

## Description

Start sending cyclic messages again after AREthILControlWait.

Application Endpoints and Provided Services do not have to be created again.

## Return Values

0: The function was successfully executed

## Example

```c
on key 'r '
{
  // resume sending messages
  AREthILControlResume();
}
```

## Availability

| Since Version |
|---|
