# C2xSecCertificateGetSignerHandle

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecCertificateGetSignerHandle( long certificateHandle );
```

## Description

Gets the signer (parent) certificate of a certificate.

## Parameters

| Name | Description |
|---|---|
| certificateHandle | Handle of the certificate |

## Example

```c
long certificateHandle;
long signerHandle;
certificateHandle = C2xSecCertificateGetHandle( "MyCert" );
if (certificateHandle != 0)
{
  signerHandle = C2xSecCertificateGetSignerHandle(certificateHandle);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | — | — | — | 2.1 SP3 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
