# diagInitialize

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagInitialize( diagResponse object, char serviceQualifier[]); // form 1
```

## Description

Reinitializes the object for the given service or primitive. Diagnostics request will be initialized with the default request parameters of the service, while diagnostic responses will be initialized with the default parameters of the first or specified primitive of the service. If the service is not defined, or the primitive is not defined at the given service, nothing happens and an error code is returned.

The data contained in the primitive is overwritten by a successful call of this function!

Please refer to diagnostic descriptions with overloaded responses for details on services defining more than one response.

## Return Values

0: No error, OK

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

| Since Version |
|---|
