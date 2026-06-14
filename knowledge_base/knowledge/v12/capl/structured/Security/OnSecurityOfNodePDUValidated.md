# OnSecurityOfNodePDUValidated

> Category: `Security` | Type: `function`

## Syntax

```c
void OnSecurityOfNodePDUValidated(char nodeName[], char networkName[], char pduName[], dword dataId, byte payload[], dword payloadLength, qword authInfoHigh, qword authInfo, dword authInfoBitLength, qword freshness, dword freshnessBitLength, dword freshnessValueId, dword verificationResult)
```

## Description

This callback handler is called, when a node received a secured PDU and verified the authentication information.

Apart from the verification result, all values which have been used for verification can be analyzed.

You have to call SecurityLocalStartControlSimulationNode before this callback is called.

## Return Values

—

## Example

```c
// this example does an write output for every secured pdu which is received.
void OnSecurityLocalPDUValidated(char nodeName[], char networkName[], char pduName[], dword dataId, byte payload[], dword payloadLength, qword authInfoHigh, qword authInfo, dword authInfoBitLength, qword freshness, dword freshnessBitLength, dword freshnessValueId, dword verificationResult)
{
  if (verificationResult > 0)
    {
      writeLineEx(1,0," Verification SUCCESSFUL");
    }
    else
    {
      writeLineEx(1,3," Verification FAILED");
    }
}
```

## Availability

| Since Version |
|---|
