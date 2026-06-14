# C2xEnableMsg

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xEnableMsg (char* dbMessage);
```

## Description

Enables a message for which the database attribute Send Type is Cyclic or CyclicIfActive in the database for cyclic sending. The function has no effect for messages with Send Type NoMsgSendType.

## Return Values

0 or error code

## Availability

| Since Version |
|---|
