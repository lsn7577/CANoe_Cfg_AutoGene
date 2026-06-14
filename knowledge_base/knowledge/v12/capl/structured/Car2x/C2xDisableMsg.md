# C2xDisableMsg

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xDisableMsg (char* dbMessage);
```

## Description

Disables a message for which the database attribute Send Type is Cyclic or CyclicIfActive in the database for cyclic sending. The function has no effect for messages with Send Type NoMsgSendType.

## Return Values

0 or error code

## Example

```c
C2xDisableMsg("CAM");
```

## Availability

| Since Version |
|---|
