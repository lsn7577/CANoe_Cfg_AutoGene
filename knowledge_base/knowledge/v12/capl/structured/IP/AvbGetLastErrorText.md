# AvbGetLastErrorText

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbGetLastErrorText(dword bufferLength, char buffer[]);
```

## Description

Function to retrieve the last error which occurs in the AVB IL as string.

The call of the AvbGetLastErrorText function does not reset the saved error text.

## Return Values

Number of copied characters.

## Example

```c
char buffer[1024];
dword listenerHandle;

// open a listener
listenerHandle = AvbOpenListener();

// check if last function was executed successfully
if ((AvbGetLastErrorText(elcount(buffer), buffer)) != 0)
{
  write("AVB IL error occurred: %s", buffer);
}
```

## Availability

| Since Version |
|---|
