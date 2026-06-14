# diagIsNegativeResponse

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagIsNegativeResponse (diagResponse obj)
```

## Description

Returns value <> 0 if the object is a negative response to a request.

## Return Values

0 or <>0

## Example

```c
on diagResponse *
{
  // Handle the ambiguity of neg responses by treating them as '*'
  if( diagIsNegativeResponse ( this ) )
  {
    write( "Received negative response for service 0x%x, code 0x%x",
    (long) diagGetParameter( this, "SIDRQ_NR" ),
    (long) diagGetParameter( this, "NRC" ) );
  }
}
```

## Availability

| Since Version |
|---|
