# OnSecurityLocalApplicationProtocolRxFinished

> Category: `Security` | Type: `function`

## Syntax

```c
void OnSecurityLocalApplicationProtocolRxFinished(char applicationProtocolName[], byte payload[], dword payloadLength, long result)
```

## Description

This callback handler is called when the reception of an application protocol is finished.

As the behavior of application protocols are Security specific you have to refer to the Security Source specific manual to get more information about how they work.

You have to call SecurityLocalStartControlSimulationNode before this callback is called.

## Availability

| Since Version |
|---|
