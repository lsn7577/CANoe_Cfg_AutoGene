# GPIBOnError

> Category: `GPIB` | Type: `function`

## Syntax

```c
GPIBOnError (long deviceDescriptor, char query[], char response[], long status, long error);
```

## Description

This optional function is called if a query or a write operation (GPIBWriteStr or GPIBWriteNum) raised an error condition.

Users may implement this function and then receive the original query string or the data to be written, respectively. The result string, if any, is also returned, as well as the GPIB status word, the error code and the device descriptor.

## Return Values

—

## Availability

| Since Version |
|---|
