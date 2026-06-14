# linConfigureResponse

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linConfigureResponse(dword frameId, dword dlc, byte[] responseData); // form 1
```

## Description

Configures a response frame of a LIN node if no database is used.

This function may only be called in the event procedure on preStart.

## Return Values

Returns 1 if the configuration of the response succeeded, otherwise 0.

## Example

```c
// Configure the LIN frame with the ID 0x01 as response of the slave and initialize the value of all response bytes to zero.

on preStart

{
  long i;
  byte responseData [8];

  for(i = 0; i < 8; i++)
  {
    responseData [i] = 0;
  }

  linConfigureResponse(0x01, 8, responseData);
}
```

## Availability

| Since Version |
|---|
