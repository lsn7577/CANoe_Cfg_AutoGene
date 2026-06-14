# C2xSecCertificateGetSignerHandle

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecCertificateGetSignerHandle( long certificateHandle );
```

## Description

Gets the signer (parent) certificate of a certificate.

## Return Values

Handle of the signer (parent) certificate or 0

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

| Since Version |
|---|
