# diagInitialize

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagInitialize( diagResponse object, char serviceQualifier[]); // form 1
long diagInitialize( diagResponse object, char serviceQualifier[], char primitiveQualifier[]); // form 2
long diagInitialize( diagRequest object, char serviceQualifier[]); // form 3
long DiagInitialize(diagRequest object); // form 4
long DiagInitialize(diagResponse object); // form 5
```

## Description

Reinitializes the object for the given service or primitive. Diagnostics request will be initialized with the default request parameters of the service, while diagnostic responses will be initialized with the default parameters of the first or specified primitive of the service. If the service is not defined, or the primitive is not defined at the given service, nothing happens and an error code is returned.

## Parameters

| Name | Description |
|---|---|
| object | Diagnostics object to re-initialize |
| serviceQualifier | Qualifier of the service that should be used for reinterpretation |
| primitiveQualifier | Qualifier of the service primitive that should be used for reinterpretation |

## Example

In an ECU simulation, initialize a response object with a specific primitive before sending it.

```c
on diagRequest Servi 
{
   diagResponse this response; // will be initialized with first primitive 
   response.Initialize( "Servi", "ServiEcu1PR"); // Force initialization with specific primitive 
   response.SetParameter( "Voltage", 28.0); // Access primitive specific parameter 
   response.SendResponse();
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2: form 1, 2, 3 9.0 SP3: form 4, 5 | 7.1 SP3: form 1, 2, 3 9.0 SP3: form 4, 5 | — | — | — | 1.0: form 1, 2, 3 2.1 SP3: form 4, 5 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
