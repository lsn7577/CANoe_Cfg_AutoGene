# SCC_GetCertChainVerificationError

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_GetCertChainVerificationError (dword Index, char CertName[], dword& ErrorCode)
```

## Description

Returns an individual verification from the last certificate chain verification, which is indicated by the callback function SCC_CertChainVerificationInd.

## Parameters

| Name | Description |
|---|---|
| Index | Number of the queried error GetCertChainVerificationErrorCount. |
| CertName | Returns the name of the verified certificate (to the output buffer). The same certificate may be returned multiple times with different error codes. |
| 1 | Certificate serial negative |
| 2 | Distinguished Name too long |
| 3 | Signature method too weak |
| 4 | Untrusted hash |
| 5 | Certificate not yet valid |
| 6 | Certficiate has expired |
| 7 | Certficiate issuer not found |
| 8 | Cannot establish trust |
| 9 | Certificate chain loop |
| 10 | Chain lacks trusted root |
| 11 | Chain name mismatch |
| 12 | Policy error |
| 13 | Invalid usage |
| 14 | Certificate chain too long |
| 15 | Certificate issuer is not a valid CA |
| 16 | Name constraint error |
| 17 | Certificate ssuer not found |
| 18 | Unknown critical extension |
| 19 | Duplicate certificate extension |
| 20 | Invalid X.509v3 extension in v1 or v2 certificate |
| 21 | Duplicate certificate policy |
| 22 | X.509v2 identifiers in v1 certificate |
| 23 | Signature error |
| 24 | Certificiate public key invalid |
| 25 | Signature algorithm unknown |
| 26 | Signature algorithm – bad parameters |
| 101 | Domain Component invalid according to ISO 15118-2 |

## Example

```c
SCC_CertChainVerificationInd( byte SessionId[], char ChainName[], dword Result )
{
  int i;
  char certName[255];
  dword errorCode;

  if (Result == 0)
  {
    for (i = 0; i < SCC_GetCertChainVerificationErrorCount(); ++i)
    {
      SCC_GetCertChainVerificationError(i, certName, errorCode);

      WriteLineEx(1 /* CAPL */, 2 /* warning */, "Certificate %s of %s verified with Error: %i", certName, chainName, errorCode);
    }
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 15 | — | — | — | — |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
