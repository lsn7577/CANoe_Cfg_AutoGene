# C2xSecCertificateCreate

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecCertificateCreate(long originalCertificateHandle, dword validityInSeconds);
long C2xSecCertificateCreate(long originalCertificateHandle, dword validityInSeconds, long signerCertificateHandle);
```

## Description

Generate a new certificate based on another certificate.

The certificate is only valid while the measurement is running and it is automatically discarded afterwards.

The certificate is only known to the real-time part of CANoe. The analysis part only gets knowledge of it when it is transmitted in a message.

## Parameters

| Name | Description |
|---|---|
| originalCertificateHandle | Handle of a certificate which is used as a template.The new certificate inherits all properties of the original certificate except the key pair and those properties specified by the other parameters below. |
| validityInSeconds | The new certificate is at least valid for the specified seconds past the current CANoe simulation time. The validity period of the new certificate starts at midnight of the current simulation day. |
| signerCertificateHandle | Handle to a certificate to be used as certificate signer. If this parameter is omitted, the original certificate’s signer is used. If the orignial certificate is a Root (self signed) certificate this parameter has no meaning. To use a certificate as signer the matching private key must be known and the signer certificate’s protocol version must match that of the one to be signed. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 | — | — | — | 2.2 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
