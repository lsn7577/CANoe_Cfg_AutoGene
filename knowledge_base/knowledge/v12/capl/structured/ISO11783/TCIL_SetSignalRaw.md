# TCIL_SetSignalRaw

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_SetSignalRaw( dbSignal signal, long value );
```

## Description

Sets the signal to the specified raw value. The message of the signal is sent according the configured send type.

## Return Values

0: Function has been executed successfully

## Example

```c
void SendLanguageCommand_English()
{
  TCIL_SetSignalRaw( LC_TC::LanguageCodeCmd, 0x6E65 );
}
```

## Availability

| Since Version |
|---|
