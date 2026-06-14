# LocalSecurityCalculateAuthenticator

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long LocalSecurityCalculateAuthenticator (dword DATAID, byte[] Payload, dword PayloadLength, qword TruncatedAuthenticator, dword TruncatedAuthenticatorBitLength, qword Freshness, dword TruncatedFreshnessBitLength, dword FreshnessValueBitLength)
```

## Description

Calculates the authenticator (CMAC) for the given payload and freshness. This function can be used for testing.

## Return Values

A value <= 0 means error
Value 1 means action was successful.

## Example

```c
/// The Method LocalSecurityCalculateAuthenticator can be used to calculate the Authenticator on your own with an own maintained freshness value
/// It is used for testing the local algorithm and to calculate an authanticator with a given freshness, payload and data id
/// With LocalSecurityVerifyAuthenticationInformation the information generated with LocalSecurityCalculateAuthenticator can be verified.
/// OnLocalSecurityQueryLocalFreshness in not called.
/// OnLocalSecurityPDUPreTx is not called.
/// OnLocalSecurityPDUValidated is not called.
on key 'a'
{
  long bytesCopied = 0;
  qword freshnessCopy;
  dword dataID;
  byte payload[8] = {0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08};
  qword authenticator;
  dword authenticatorBitLength = 24;
  qword freshness;
  dword freshnessLength = 48;
  dword freshnessTxBitLength = 8;
  dword freshnessTxMask = 0xF;
  dword verificationResult;
  dword result;

  result = LocalSecurityCalculateAuthenticator(dataID, payload, elCount(payload), authenticator, authenticatorBitLength, freshness, freshnessTxBitLength, freshnessLength);
  Write("LocalSecurityCalculateAuthenticator result:%d", result);
  result = LocalSecurityVerifyAuthenticationInformation(dataID, payload, elCount(payload), authenticator, authenticatorBitLength, (freshness & freshnessTxMask), freshnessTxBitLength, freshness, freshnessLength, verificationResult);
  Write("LocalSecurityVerifyAuthenticationInformation result:%d, verificationResult:%d", result, verificationResult); // 1: verification successful, 0: verification failed
}
```

## Availability

| Up to Version |
|---|
