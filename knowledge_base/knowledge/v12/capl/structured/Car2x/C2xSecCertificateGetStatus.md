# C2xSecCertificateGetStatus

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecCertificateGetStatus( long certificateHandle );
```

## Description

Gets validity status of a certificate.

## Return Values

The validity status consists of 3 bit fields which are combined using a binary OR operation
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

| Since Version |
|---|
