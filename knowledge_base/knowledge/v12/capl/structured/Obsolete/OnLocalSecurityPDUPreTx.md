# OnLocalSecurityPDUPreTx

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void OnLocalSecurityPDUPreTx(char pduName[], dword dataId, byte payload[], dword payloadLength, qword& authInfo, dword authInfoBitLength, qword& freshness, dword freshnessBitLength)
```

## Description

This callback handler is called, after all data updates and the automatic Authenticator (CMAC) calculation has be done. Payload, AuthInfo and freshness can be modified in this handler before the transmission starts. Fault injection and evaluation of new algorithm are typical examples.

## Example

```c
/// This callback can be used to inject faults.
/// This callback is called after the CMAC is calculated for a PDU to send
/// You can change the truncated freshness, the truncated calculated authenticator or the payload - the values which are part of the Secured-I-PDU
void OnLocalSecurityPDUPreTx(char pduName[], dword dataId, byte payload[], dword payloadLength, qword& truncatedAuthInfo, dword truncatedAuthInfoBitLength, qword& truncatedFreshness, dword truncatedFreshnessBitLength)
{
  if (dataId == 1)
  {
    truncatedAuthInfo = 0x123456; // change cmac
    // truncatedFreshness = 0x02; // change freshness
    // payload[0] = 0xFF; // change payload;
  }
}
```

## Availability

| Up to Version |
|---|
