# AfdxGetTokenReal

> Category: `ADFX` | Type: `function`

## Syntax

```c
float AfdxGetTokenReal( long packet, char protocolDesignator[], char tokenDesignator[], long offset, long length );
```

## Description

This function returns the specified token's data as a float value.

## Return Values

integer value gathered from the token's data
With AfdxGetLastError you have to check if the function has been processed successfully.

## Example

```c
void OnAfdxPacket(long channel, long dir, long flags, long bag, long packet )
{
  double temperature;
  char error[100];

  // get temperature value from payload position 8 as a float (4byte length)
  temperature = AfdxGetTokenReal( packet, "udp", "data", 8, 4 );

  if (AfdxGetLastError() == 0)
  {
    // do something with temperature
  }
  else
  {
    AfdxGetLastErrorText( elCount(error), error );
    write("Error: %s", error );
  }
}
```

## Availability

| Since Version |
|---|
