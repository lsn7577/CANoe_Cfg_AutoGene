# diagCheckValidPrimitive

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagCheckValidPrimitive( diagRequest obj);
```

## Description

Returns 1 if the response received for the request matches its specification in the diagnostic description. If a primitive qualifier is given, the definition of that primitive at the object's service is used as specification.

If the primitive is not valid, 0 is returned and the optional parameter reasonOut[0] is set to the precise reason why the check failed (see below).

If a primitive is specified, it must be defined for the service the response currently refers to! Please refer to diagnostic descriptions with overloaded responses for details.

## Return Values

1: Primitive matches the specification in the diagnostic description.

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

| Since Version |
|---|
