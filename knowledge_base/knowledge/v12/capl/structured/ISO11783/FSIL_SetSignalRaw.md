# FSIL_SetSignalRaw

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_SetSignalRaw( dbSignal signal, long value );
```

## Description

Sets the signal to the specified raw value. The message of the signal is sent according the configured send type.

## Return Values

0: Function has been executed successfully

## Example

```c
void SendLanguageCommand_English()
{
  FSIL_SetSignalRaw( LC_FS::LanguageCodeCmd, 0x6E65 );
}
```

## Availability

| Since Version |
|---|
