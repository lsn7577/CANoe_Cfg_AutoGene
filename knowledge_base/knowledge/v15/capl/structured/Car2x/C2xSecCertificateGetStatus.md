# C2xSecCertificateGetStatus

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecCertificateGetStatus( long certificateHandle );
```

## Description

Gets validity status of a certificate.

## Parameters

| Name | Description |
|---|---|
| certificateHandle | Handle of the certificate |

## Return Values

The validity status consists of 3 bit fields which are combined using a binary OR operation.
The overall status is masked with 0xf000 and has the meaning:
The relevant subject in the trust chain is identified by the mask 0x0f00:
In case of an invalid status the reason is specified by the mask 0x000f:
Status examples:

## Example

```c
long certificateHandle;
certificateHandle = C2xSecCertificateGetHandle( "MyCert" );
switch (C2xSecCertificateGetStatus(certificateHandle) & 0xF000)
{
  case 0x1000: // unknown
    break;
  case 0x2000: // invalid
    break;
  case 0x3000: // valid
    break;
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
