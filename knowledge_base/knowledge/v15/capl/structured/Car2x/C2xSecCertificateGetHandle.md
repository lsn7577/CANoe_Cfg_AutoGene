# C2xSecCertificateGetHandle

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecCertificateGetHandle( char name[] );
long C2xSecCertificateGetHandle( byte hashedId8[] );
```

## Description

Gets a certificate handle from a certificate listed in the Car2x Certificate Manager.

## Parameters

| Name | Description |
|---|---|
| name | Name of the certificate as it is given in the Car2x Certificate Manager. |
| hashedId8 | hashedId8 digest of the certificate (e.g. included in the security header of a received frame), size must be 8 bytes. In some protocols this parameter is called certId8. |

## Example

```c
// assumes a certificate with name "MyCert" was added to the configuration in the Car2x Certificate Manager dialog

long certificateHandle;
certificateHandle = C2xSecCertificateGetHandle( "MyCert" );
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
