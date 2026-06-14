# J1939TableTime

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939TableTime( char busName[] );
```

## Description

The function returns the time stamp of the last received "Request for Address Claim". Use this function to determine, if the network table is up to data.

## Return Values

time stamp of the last received Request for Address Claim in 10µs

## Example

```c
dword time;
time = J1939TableTime( "default" 
 );

if (time + 25000 < timeNow()) 
 {
write( "Last Request for ACL is older than 250ms" );
}
```

## Availability

| Since Version |
|---|
