# OnLocalSecurityPDUValidated

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void OnLocalSecurityPDUValidated(char pduName[], dword dataId, byte payload[], long payloadLength, qword authInfo, dword authInfoBitLength, qword freshness, dword freshnessBitLength, dword verificationResult)
```

## Description

This callback handler is called, when a secured PDU is received in the node. Besides to the verification result all values which have been used for verification can be analyzed.

## Availability

| Up to Version |
|---|
