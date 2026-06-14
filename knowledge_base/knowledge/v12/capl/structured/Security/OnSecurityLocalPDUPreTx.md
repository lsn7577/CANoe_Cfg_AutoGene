# OnSecurityLocalPDUPreTx

> Category: `Security` | Type: `function`

## Syntax

```c
void OnSecurityLocalPDUPreTx(char pduName[], dword dataId, byte payload[], dword payloadLength, qword& authInfo, dword authInfoBitLength, qword& freshness, dword freshnessBitLength)
```

## Description

This callback handler is called, after all data updates and the automatic Authenticator (CMAC) calculation has be done. Payload, AuthInfo and freshness can be modified in this handler before the transmission starts. Fault injection and evaluation of new algorithm are typical examples.

## Return Values

byte payload[]
The payload of the PDU.

## Example

```c
// this example modifies the MAC of PDU with Data ID 1
void OnSecurityLocalPDUPreTx(char pduName[], dword dataId, byte payload[], dword payloadLength, qword& authInfoHigh, qword& authInfo, dword authInfoBitLength, qword& freshness, dword freshnessBitLength, dword freshnessValueId)
{
  if (dataId == 1)
  {
    authInfo = 0x123456; // change cmac
    // freshness = 0x02; // change freshness
    // payload[0] = 0xFF; // change payload;
  }
}
```

## Availability

| Since Version |
|---|
