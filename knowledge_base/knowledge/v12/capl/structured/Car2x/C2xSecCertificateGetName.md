# C2xSecCertificateGetName

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecCertificateGetName( long certificateHandle, long length, char name[] );
```

## Description

Gets a certificate name from Car2x Certificate Manager.

## Return Values

0 or error code

## Example

```c
// assumes a certificate with this certificateHandle is available in the Car2x Certificate Manager
long certificateHandle;
char certName[100];
long errCode;

errCode = C2xSecCertificateGetName( certificateHandle, elCount(certName), certName );
```

## Availability

| Since Version |
|---|
