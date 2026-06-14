# SecurityOfNodeSetKey

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityOfNodeSetKey(char nodeName[], char networkName[], char keyIdentifierString[], dword keyIdentifierValue, byte newKey[], dword keyLength, dword flags)
```

## Description

Changes a key at the node the specified node on the specified network.

As keys and the key handling differs from Security Source to Security Source you have to refer to the Security Source specific manual to get more information about which values you have to specify as parameters.

You have to call SecurityLocalStartControlSimulationNode before this callback is called.

## Return Values

1: SuccessA Value of 1 means that the action was successful. A value less than or equal to 0 means error.

## Availability

| Since Version |
|---|
