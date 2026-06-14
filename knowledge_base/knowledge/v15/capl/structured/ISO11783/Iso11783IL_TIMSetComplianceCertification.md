# Iso11783IL_TIMSetComplianceCertification

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetComplianceCertification(dword testProtocolPublicationYear, dword testProtocolRevision, dword laboratoryType, dword laboratoryID, dword referenceNumber); // form 1
long Iso11783IL_TIMSetComplianceCertification(dbNode participant, dword testProtocolPublicationYear, dword testProtocolRevision, dword laboratoryType, dword laboratoryID, dword referenceNumber); // form 2
```

## Description

Sets the content of message ISOBUS Compliance Certification (see ISO11783-7 B.27).

If the ISOBUS Compliance Certification message is in the Tx list of the TIM node and a Request for PGN 64834 (FD42h) is received then the ISOBUS Compliance Certification message is sent using the specified parameter (ISOBUS Compliance Certification message revision is always 1).

## Parameters

| Name | Description |
|---|---|
| testProtocolPublicationYear | The publication year of the compliance test protocol to which the certification test was performed. Range: 2000..2061. |
| testProtocolRevision | Revision of the compliance test performed. Range: 0..31. |
| Function ID | Description |
| 0 | Non-certified laboratory/self-certification |
| 1 | AEF certified laboratory |
| 2 | Reserved |
| 3 | Not available (not certified) |
| laboratoryID | Manufacturer code of the laboratory that performed the compliance test. Range: 0..2047. |
| referenceNumber | Certification reference number assigned by a certification laboratory. Range: 0..65355. |
| participant | TIM participant (TIM server or TIM client). |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | 13.0 | — | — | 3.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
