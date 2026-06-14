# diagInterpretAs

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagInterpretAs( diagResponse response, char primitiveQualifier[]);
```

## Description

Treats the data of the response object as the specified primitive. This will cause a reinterpretation of the data, but the data will not be changed.

The specified primitive must be defined for the service the response currently refers to! Please refer to diagnostic descriptions with overloaded responses for details.

## Return Values

0: No error, OK

## Example

This function determines the actual response primitive by trying to set the interpretation of the argument to the defined variations. 0 is returned if interpretation is possible.

```c
long FindCorrectInterpretation( diagResponse * response)
{
   if( !response.InterpretAs( "ServiPR"))
      return 0; // no error -> interpretation OK
   if( !response.InterpretAs( "ServiEcu1PR"))
      return 0; // no error -> interpretation OK
   if( !response.InterpretAs( "ServiDefauD"))
      return 0; // no error -> interpretation OK
   // None of the known primitives matches, so return failure
   return -1; // not found
}
```

## Availability

| Since Version |
|---|
