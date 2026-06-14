# SecurityOfNodeCalculateAuthenticator

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityOfNodeCalculateAuthenticator(char nodeName[], char networkName[], dword dataId, byte payload[], dword payloadLength, qword truncatedAuthenticatorHigh, qword truncatedAuthenticator, dword truncatedAuthenticatorBitLength, qword freshness, dword truncatedFreshnessBitLength, dword freshnessValueBitLength, dword freshnessValueId)
```

## Description

Calculate the authenticator from arbitrary data. The (complete) freshness value must be provided in the function call. Other freshness sources will be ignored. The method returns the truncated freshness via freshness' parameter. The calculated authenticator is returned via the TruncatedAuthenticator parameter. The truncated bit lengths of the authenticator and freshness can be modified.

The result of this method depends on the security profile which is mapped on the network.

You have to call SecurityLocalStartControlSimulationNode before this callback is called.

## Return Values

1: SuccessA Value of 1 means that the action was successful. A value less than or equal to 0 means error.

## Availability

| Since Version |
|---|
