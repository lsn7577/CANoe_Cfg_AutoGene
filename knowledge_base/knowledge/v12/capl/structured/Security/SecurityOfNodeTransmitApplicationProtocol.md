# SecurityOfNodeTransmitApplicationProtocol

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityOfNodeTransmitApplicationProtocol(char nodeName[], char networkName[], char applicationProtocolUserDefinedId[], byte payload[], dword payloadLength)
```

## Description

Transmits a special message of sequence of message protocol from the specified node on the specified network, specifically to the active Security Profile on the network.

The application protocol is specific to the active Security Profile on the network. Please refer to the Security Source specific manual to get more information about if there are application protocols available and their functionality and purpose.

You have to call SecurityLocalStartControlSimulationNode before this callback is called.

## Return Values

1: SuccessA Value of 1 means that the action was successful. A value less than or equal to 0 means error.

## Availability

| Since Version |
|---|
