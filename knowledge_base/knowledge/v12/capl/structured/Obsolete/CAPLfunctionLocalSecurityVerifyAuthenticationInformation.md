# CAPLfunctionLocalSecurityVerifyAuthenticationInformation

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long LocalSecurityVerifyAuthenticationInformation (dword DATAID, byte[] Payload, dword PayloadLength, qword TruncatedAuthenticator, dword TruncatedAuthenticatorBitLength, qword RxFreshnessh, dword RxFreshnessBitLength, qword currentFreshness, dword FreshnessValueBitLength dword ValidationResult)
```

## Description

Verifies the specified authentication information (CMAC and freshness) of the PDU. The payload is also an input parameter to the verification logic.

## Return Values

A value <= 0 means error
Value 1 means action was successful.

## Availability

| Up to Version |
|---|
