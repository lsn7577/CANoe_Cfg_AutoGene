# C2xSecCertificateValidAppSspBitmap

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecCertificateValidAppSspBitmap(long certHdl, dword aid, dword sspLen, byte ssp[], byte msk[], dword checkChain)
```

## Description

Validates the Service Specific Permission (SSP) bit mask of a certificate.

## Parameters

| Name | Description |
|---|---|
| certHdl | Handle of the certificate to be tested. |
| aid | Application ID / PSID. |
| sspLen | Length of the byte arrays ssp and msk (mask). |
| ssp Byte Array | The SSP to be tested. |
| msk Byte Array | Mask of the bits in the SSP array to be compared. |
| checkChain | If set to 1, the whole certificate chain is tested (recommended). |

## Example

```c
variables
{
  dword myCertHdl;

  struct SspBitmap
  {
    char  name[16];
    dword aid;
    dword len;
    byte  ssp[10];
    byte  msk[10];
    byte  chain;
  };

  struct SspBitmap ssp =
  {
    "CAM",
    0x24,
    3,
    { 0x01, 0x02, 0x00 },
    { 0xff, 0x02, 0x00 },
    1
  };
}

on start
{
  myCertHdl = C2xSecCertificateGetHandle("MyCert");

  write("SSP %s: %d", ssp.name,
    C2xSecCertificateValidAppSspBitmap(myCertHdl, ssp.aid,
    ssp.len, ssp.ssp, ssp.msk, ssp.chain)) ;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | — | — | — | 5.0 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
