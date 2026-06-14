# diagIsValidValue

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagIsValidValue( diagResponse response, char[] parameterQualifier, long[] errorLevelOut);
```

## Description

Returns 1 if the parameter in the response object is valid, otherwise 0 is returned and the level of the problem (error or warning) is set in the output parameter field.

## Return Values

1: Parameter value is valid, errorLevelOut[0] is set to 0.

## Example

```c
on diagResponse Example_Service
{
   long errorLevelOut[1];
   long status;
   status = diagIsValidValue( this, "MyParameter", errorLevelOut);
   if( status == 1)
   {
      write( "Parameter value OK");
   } else if( status == 0)
   {
      if( errorLevelOut[0] == 1)
         write( "Warning.");
      else if( errorLevelOut[0] == 2)
         write( "ERROR!");
   } else
   {
      write( "Error %d checking parameter value!", status);
   }
}
```

## Availability

| Since Version |
|---|
