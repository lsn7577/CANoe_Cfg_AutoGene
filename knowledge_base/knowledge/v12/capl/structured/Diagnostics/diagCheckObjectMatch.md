# diagCheckObjectMatch

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagCheckObjectMatch( diagRequest request, diagResponse response);
```

## Description

Checks if the response service id is a valid (positive or negative) response for the request.

## Return Values

1: Objects match.

## Example

```c
DiagRequest AirbaContr_Read req;
DiagResponse AirbaContr_Read resp;

if( 1 == diagCheckObjectMatch( req, resp))
write( "Request and response match!");
```

## Availability

| Since Version |
|---|
