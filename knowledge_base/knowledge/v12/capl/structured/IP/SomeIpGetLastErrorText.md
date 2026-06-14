# SomeIpGetLastErrorText

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpGetLastErrorText( dword bufferLength, CHAR buffer[] );
```

## Description

Interface to retrieve the last error which occurs in the SOME/IP IL as string.

If the last called function has been successfully executed, the value 0 is returned. The call of the SomeIpGetLastErrorText function does not reset the saved error text.

## Return Values

Number of copied characters

## Example

```c
char buffer[1024];

// resume sending messages
SomeIpILControlResume();

// check if last function was executed correct
if((SomeIpGetLastErrorText(elcount(buffer),buffer)) != 0)
{
  write("SOME/IP IL error occurred: %s", buffer);
} // if
```

## Availability

| Since Version |
|---|
