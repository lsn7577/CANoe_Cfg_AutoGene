# diagGetComplexParameter

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetComplexParameter (diagResponse obj, char parameterName[], dword iteration, char* subParameter, double output[1])
```

## Description

Retrieve numeric sub-parameter from a parameter iteration directly.

## Return Values

Error code
or value of the parameter or 0.0 if this could not be acquired.

## Example

```c
on diagResponse Door.FaultMemory_ReadAllIdentified
{
  dword DTC;
  char DTCasText[100];
  int i;

  if(diagIsPositiveResponse(this))
  {
    // Iterate over the list of DTCs and retrieve the numeric and symbolic value of each DTC
    for(i=0;i<DiagGetIterationCount(this,"ListOfDTC");i++)
    {
      DTC=DiagGetComplexParameter(this,"ListOfDTC",i,"DTC");
      DiagGetComplexParameter(this,"ListOfDTC", i, "DTC" , DTCasText, elCount(DTCasText));
      write("DTC %06X - %s",DTC, DTCasText);
    }
  }
  else
  {
    write("Negative response received.\nNegative response code: 0x%02X", (byte)DiagGetResponseCode(this));
  }
}
```

## Availability

| Since Version |
|---|
