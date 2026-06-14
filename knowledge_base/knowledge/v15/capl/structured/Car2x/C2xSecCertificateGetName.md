# C2xSecCertificateGetName

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecCertificateGetName( long certificateHandle, long length, char name[] );
```

## Description

Gets a certificate name from Car2x Certificate Manager.

## Parameters

| Name | Description |
|---|---|
| certificateHandle | Handle of the certificate. |
| length | Maximum number of bytes to be copied; make sure size of destination is equal or larger than length of name[]. |
| name | Buffer in which the name is copied. |

## Example

```c
// assumes a certificate with this certificateHandle is available in the Car2x Certificate Manager
long certificateHandle;
char certName[100];
long errCode;

errCode = C2xSecCertificateGetName( certificateHandle, elCount(certName), certName );
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
