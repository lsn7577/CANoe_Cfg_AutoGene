# diagIsRespParameterDefault

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagIsRespParameterDefault (diagRequest obj, char parameterName[])
```

## Description

Access/check a response parameter for a given request. It is not necessary to declare the response and retrieve the response explicitly e.g. via diagGetLastReponse(diagRequest) to make a check with diagResponse.IsParameterDefault("MyParamName").

## Parameters

| Name | Description |
|---|---|
| obj | Diagnostics request |
| parameterName | Parameter qualifier |

## Example

```c
testfunction MainTest()
{
   diagRequest DefaultSession_Start req;
   diagSetTarget("Door");
   diagSendRequest(req);
   testWaitForDiagResponse(req, 2000);
   write("IsDefault(P3) = %d", diagIsRespParameterDefault(req, "P3"));
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 | — | — | — | 1.0 |
| Restricted To | — | Online mode Not for basic diagnostics | — | — | — | Online mode Not for basic diagnostics |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
