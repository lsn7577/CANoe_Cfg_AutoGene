# mostParamSetData

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostParamSetData(mostAmsMessage msg, char paramadr[], byte data[], long datalen)
```

## Description

Setting of parameters of the String type or RawStream in an AMS message using the parameter name from the XML function catalog.

When writing a string parameter with mostParamSetData 'data' has to include the coding byte and terminator character (mostParamSetString can be used for ASCII coding).

The message data must contain a parameter with the given parameter address.

Since the compiler is not able to validate this, errors are detected at run time of the CAPL program only. If the parameter is not part of the message or not the expected type, an error text is displayed in the Write Window and the measurement stops. The function mostParamIsAvailable can be applied to assure parameter availability.

When using function mostParamSetData to build a message dump, the parameters must be populated in the order specified by the MOST Function Catalog, particularly for messages with StreamCases.

## Return Values

See error codes

## Availability

| Since Version |
|---|
