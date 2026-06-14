# OnSecurityOfNodeApplicationProtocolRxFinished

> Category: `Security` | Type: `function`

## Syntax

```c
void OnSecurityOfNodeApplicationProtocolRxFinished(char nodeName[], char networkName[], char applicationProtocolName[], byte payload[], dword payloadLength, long result)
```

## Description

This callback handler is called when the specified node on the specified network finished the reception of an application protocol.

As the behavior of application protocols are Security specific you have to refer to the Security Source specific manual to get more information about how they work.

You have to call SecurityLocalStartControlSimulationNode before this callback is called.

## Return Values

—

## Availability

| Since Version |
|---|
