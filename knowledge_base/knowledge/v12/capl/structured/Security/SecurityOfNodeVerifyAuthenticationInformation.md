# SecurityOfNodeVerifyAuthenticationInformation

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalVerifyAuthenticationInformation(dword dataId, byte payload[], dword payloadLength, qword truncatedAuthenticatorHigh, qword truncatedAuthenticator, dword truncatedAuthenticatorBitLength, qword rxFreshness, dword rxFreshnessBitLength, qword currentFreshness, dword freshnessValueLength, dword freshnessValueId, dword verificationResult)
```

## Description

Verifies the specified authentication information (MAC and freshness) of the PDU. The (complete) current freshness value must be provided in the function call. Other freshness sources will be ignored. The payload is also an input parameter to the verification logic.

The result of this method depends on the security profile which is mapped on the network.

You have to call SecurityLocalStartControlSimulationNode before this callback is called.

## Return Values

dword verificationResult [Out]

## Availability

| Since Version |
|---|
