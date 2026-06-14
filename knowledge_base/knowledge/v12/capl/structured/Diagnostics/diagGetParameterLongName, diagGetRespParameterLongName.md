# diagGetParameterLongName, diagGetRespParameterLongName

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
diagGetParameterLongName, diagGetRespParameterLongName(obj);
```

## Description

Copies the long name of a diagnostic parameter into the buffer, honoring the character encoding configured in the diagnostic description. The text is converted into the encoding used in the CAPL program.

There are two ways to identify the parameter:

## Parameters

| Name | Description |
|---|---|
| obj | Diagnostic object. |

## Return Values

Length of path written to buffer, may be truncated.

## Example

```c
// Write the parameter paths, names and symbolic values of a response object to the Write Window
DumpResponseParameterPaths( DiagResponse * resp)
{
  WORD i;
  char path[100];

  resp.GetObjectPath( path, elcount( path));
  write( "Object: %s", path);

  i = 0;
  while( resp.GetParameterPath( i, path, elcount( path)) > 0)
  {
    char parameterSymbol[200];
    char name[200];
    resp.GetParameter( path, parameterSymbol, elcount( parameterSymbol));
    DiagGetParameterLongName( resp, path, name, elcount(name));
    write( "%2i %-50s %-20s = %s", i, path, name, parameterSymbol);
    ++i;
  }
}
```

## Availability

| Since Version |
|---|
