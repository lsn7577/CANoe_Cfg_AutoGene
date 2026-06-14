# Iso11783IL_TIMGetProperty

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMGetProperty(char propertyName[]); // form 1
long Iso11783IL_TIMGetProperty(dbNode participant, char propertyName[]); // form 2
```

## Description

Gets a property of the TIM server/client.

## Parameters

| Name | Type | Description |
|---|---|---|
| Properties | Value Range | Description |
| isServerMaster | 0..1 | 1: TIM server is TIM server master. 0: TIM server is no TIM server master. |
| bootTime | 0..255 [seconds] | Boot time which is reported in the TIM_ServerVersionResponse message. |
| minimumVersion | 0..255 | Minimum TIM version number of the TIM client/server. |
| implementedVersion | 0..255 | Implemented TIM version number of the TIM client/server. |
| deactivateCertificateValidation | 0..FFh | Bit 0 = 1: Validation of Conformance Certification information against device certificate is deactivated. The parameter group ‘ISOBUS Compliance Certification’ is not requested. Bit 1 = 1: Validation of ISOBUS device name (NAME) against device certificate is deactivated. Bit 2 = 1: Validation of function capabilities against the certificates is deactivated. Bit 3 = 1: Check for revoked certificates is deactivated. Bit 4 = 1: Check for certificate type (client or server certificate) is deactivated. |
| enableDemoMode | 0..1 | 1: Demo mode is enabled. Therefore no certificates and keys are validated. 0: Demo mode is disabled. |
| useRequestCounter | 0..1 | 1: Increment request counter (starting with 0) in function request messages. 0: Request counter is not used when function request messages are sent. |
| restartAfterWorkflowViolation | 0..1 | 1: Client restarts communication to the server if there is a workflow violation. 0: Client does not restart communication to the server if there is a workflow violation. |
| requireAcknowledgeOfStartOfMotion | 0..1 | 1: Operator acknowledgement (Iso11783IL_TIMOperatorAcknowledgeStartOfMotion) is necessary to start vehicle motion by the client. 0: Client can start vehicle motion without operator acknowledgement. |
| participant |  | TIM participant (TIM server or TIM client). |

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
