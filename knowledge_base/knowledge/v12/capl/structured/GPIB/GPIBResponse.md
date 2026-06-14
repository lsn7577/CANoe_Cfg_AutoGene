# GPIBResponse

> Category: `GPIB` | Type: `function`

## Syntax

```c
GPIBResponse (long deviceDescriptor, char queryString[], char resultString[]);
```

## Description

This function is called when the query returns. Users must implement this function and receive the original query string, the result as a string and the device ID.

## Return Values

—

## Example

```c
char myQuery[3] = "V?";
GPIBQuery(myDevice, "V?");
...
GPIBResponse 
 (long deviceDescriptor, char queryString[], char resultString[])
{
   if 
 (deviceDescriptor == myDevice)
   {
      if 
 ( !strncmp(queryStr, myQuery))
      {
         putValue(EnvVoltage, GPIBGetFloatResult(resultString));
      }
   }
}
```

## Availability

| Since Version |
|---|
