# diagGetObjectPath

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetObjectPath (diagResponse obj, char buffer[], dword buffersize)
```

## Description

Delivers the qualifier path of the object that must be specified upon generation.

## Return Values

Length of path written to buffer, may be truncated.

## Example

```c
DumpReqParameterPaths( DiagRequest * req)
{
  DumpParameterPaths( req, 0);
}

DumpRespParameterPaths( DiagRequest * req)
{
  DumpParameterPaths( req, 1);
}

DumpParameterPaths( DiagRequest * req, long bDumpResponse)
{
  WORD i;
  char parameterPath[100];

  req.GetObjectPath( parameterPath, elcount( parameterPath));
  write( "Request is: %s", parameterPath);
  if( bDumpResponse)
    write( "Response parameters:");
  else
    write( "Request parameters:");

  i = 0;
    while( bDumpResponse && req.GetRespParameterPath( i, parameterPath, elcount( parameterPath)) > 0
    ||!bDumpResponse && req.GetParameterPath( i, parameterPath, elcount( parameterPath)) > 0)
  {
    write( "%2i %s", i, parameterPath);
    ++i;
  }
}
```

## Availability

| Since Version |
|---|
