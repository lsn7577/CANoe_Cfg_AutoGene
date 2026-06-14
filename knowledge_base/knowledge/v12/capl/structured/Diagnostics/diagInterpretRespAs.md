# diagInterpretRespAs

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagInterpretRespAs( diagRequest response, char primitiveQualifier[]);
```

## Description

Treats the data of the request's response as the specified primitive. This will cause a reinterpretation of the data, but the data will not be changed.

The specified primitive must be defined for the service the response currently refers to! Please refer to diagnostic descriptions with overloaded responses for details.

## Return Values

0: No error, OK

## Example

A tester module tries to interpret the response received for a request.

```c
if( 1 == testWaitForDiagResponse( request, 2000))
{ 
   if( 0 == diagInterpretRespAs( request, "ServiEcu1PR"))
   {
      if( 27.5 < diagGetRespParameter( request, "Voltage"))
         TestStepPass( "Voltage is high enough");
      else
         TestStepFail( "Voltage too low");
   } else
   { 
      TestStepFail( "Unexpected response version");
   }
} else
{ 
   TestStepFail( "No response received");
}
```

## Availability

| Since Version |
|---|
