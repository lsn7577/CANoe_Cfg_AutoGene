# diagCheckValidRespPrimitive

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagCheckValidRespPrimitive( diagRequest obj);
```

## Description

Returns 1 if the response received for the request matches its specification in the diagnostic description.

If the primitive is not valid, 0 is returned and the optional parameter reasonOut[0] is set to the precise reason why the check failed (see below).

If a primitive is specified, it must be defined for the service the response currently refers to! Please refer to diagnostic descriptions with overloaded responses for details.

## Return Values

1: Primitive matches its specification in the diagnostic description.

## Example

```c
if( 1 == request.CheckValidRespPrimitive( "ServiDefauD"))
   TestStepPass( "Is default response");
else
   TestStepFail( "Not default response");
```

## Availability

| Since Version |
|---|
