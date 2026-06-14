# Iso11783IL_TIMSetComplianceCertification

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetComplianceCertification(dword testProtocolPublicationYear, dword testProtocolRevision, dword laboratoryType, dword laboratoryID, dword referenceNumber); // form 1
```

## Description

Sets the content of message ISOBUS Compliance Certification (see ISO11783-7 B.27).

If the ISOBUS Compliance Certification message is in the Tx list of the TIM node and a Request for PGN 64834 (FD42h) is received then the ISOBUS Compliance Certification message is sent using the specified parameter (ISOBUS Compliance Certification message revision is always 1).

## Return Values

0: Property has been set successfully

## Availability

| Since Version |
|---|
