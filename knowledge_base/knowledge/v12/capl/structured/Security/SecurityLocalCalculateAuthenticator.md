# SecurityLocalCalculateAuthenticator

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalCalculateAuthenticator(dword dataId, byte payload[], dword payloadLength, qword truncatedAuthenticatorHigh, qword truncatedAuthenticator, dword truncatedAuthenticatorBitLength, qword freshness, dword truncatedFreshnessBitLength, dword freshnessValueBitLength, dword freshnessValueId)
```

## Description

Calculate the authenticator from arbitrary data. The (complete) freshness value must be provided in the function call. Other freshness sources will be ignored. The method returns the truncated freshness via freshness parameter. The calculated authenticator is returned via the TruncatedAuthenticator parameter. The truncated bit lengths of the authenticator and freshness can be modified.

The result of this method depends on the security profile which is mapped on the network.

## Return Values

qword truncatedAuthenticatorHigh [Out]
Upper 64 bits of the authenticator (MAC), if authenticator is larger than 64 bits. Otherwise 0;

## Availability

| Since Version |
|---|
