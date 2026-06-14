# OnSecurityOfNodeApplicationProtocolTxFinished

> Category: `Security` | Type: `function`

## Syntax

```c
void OnSecurityOfNodeApplicationProtocolTxFinished(char nodeName[], char networkName[], char applicationProtocolName[], long result)
```

## Description

This callback handler is called when the specified node on the specified network finished the transmission of an application protocol.

As the behavior of application protocols are Security specific you have to refer to the Security Source specific manual to get more information about how they work.

You have to call SecurityLocalStartControlSimulationNode before this callback is called.

## Return Values

—

## Availability

| Since Version |
|---|
