# diagGetParameter

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetParameter (diagResponse obj, char parameterName[], double output[1])
```

## Description

Returns the value of the numeric parameter, either in an output field or as return value (without the possibility of checking the correct function).

## Return Values

Error code or value of the parameter or 0.0 if this could not be acquired.

## Example

```c
// e.g. used in a Tester module
on diagResponse *
{
  byte data[4096];
  long size;
  double param_value1=0xFF;
  double param_value2=0xFF;
  diagResponse * resp;       // declare response with no concrete interpretation
  size=this.GetPrimitiveSize();             // get length of response
  this.GetPrimitiveData(data, elcount(data));  // copy actual response from "on diagResponse *" into data array
  switch(data[0]) 
  {
    case 0x50:                                // UDS: DiagnosticSessionControl_Process positive Response
      diagInitialize(resp, "DiagnosticSessionControl_Process");
      resp.Resize(size);                           // make sure there is room for the received bytes
      resp.SetPrimitiveData(data, size);           // initialize resp with actual response from data array
      param_value1=diagGetParameter(resp, "diagnosticSessionType");
      param_value2=diagGetParameter(resp, "sessionParameterRecord");
      break;
    case 0x51:                                // UDS: EcuReset_Process positive Response
      diagInitialize(resp, "EcuReset_Process");
      resp.Resize(size);                           // make sure there is room for the received bytes
      resp.SetPrimitiveData(data, size);           // initialize resp with actual response from data array
      param_value1=diagGetParameter(resp, "resetType");
      param_value2=diagGetParameter(resp, "powerDownTime");
      break;
    default:
      break;
  }
  write("Tester: Value of parameter according to chosen interpretation: 0x%x 0x%x %3.0lf %3.0lf",data[0], data[1], param_value1, param_value2);
}
```

## Availability

| Since Version |
|---|
