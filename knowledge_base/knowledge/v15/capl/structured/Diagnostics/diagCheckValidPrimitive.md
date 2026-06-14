# diagCheckValidPrimitive

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagCheckValidPrimitive( diagRequest obj);
long diagCheckValidPrimitive( diagRequest obj, dword reasonOut[]);
long diagCheckValidPrimitive( diagResponse obj);
long diagCheckValidPrimitive( diagResponse obj, dword reasonOut[]);
long diagCheckValidPrimitive( diagResponse obj, char primitiveQualifier[]);
long diagCheckValidPrimitive( diagResponse obj, char primitiveQualifier[], dword reasonOut[]);
```

## Description

Checks if the given object matches its specification in the diagnostic description.

If a primitive qualifier is given, the definition of that primitive at the object's service is used as specification.

## Parameters

| Name | Description |
|---|---|
| obj | Diagnostics object to check. |
| reasonOut | Optional output parameter field for fail reason. |
| primitiveQualifier | Qualifier of the service primitive that should be used as specification. |

## Example

```c
long ConformsToKnownPrimitives( diagResponse * response)
{
   if( 1 == response.CheckValidPrimitive( "ServiDefauD")
      || 1 == response.CheckValidPrimitive( "ServiEcu1PR"))
      return 1;
   return 0;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 7.1 SP3: form 5 and 6 7.0 SP5: methods | — | — | — | 1.0 |
| Restricted To | — | Online mode Not for basic diagnostics | — | — | — | Online mode Not for basic diagnostics |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
