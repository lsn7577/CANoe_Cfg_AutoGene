# Diagnostic Event Handlers in Analysis Branch

> Category: `Diagnostics` | Type: `notes`

## Description

In the Measurement Setup of CANoe, a diagnostic interpreter creates diagnostic request and response events for transport protocol events, if matching diagnostic descriptions have been configured.In addition to the display in the Trace Window, these events can be processed in CAPL program nodes: the event handlers on diagRequest and on diagResponse can be defined and will be called for matching objects. While it is not possible to use both types of handlers in the same CAPL node in the Simulation Setup (since a ECU does not receive responses and a tester does not receive its own requests), it is no problem to use both handler types in a CAPL node in the Measurement Setup simultaneously.

Note that certain restrictions apply to the code in these handlers.

The documentation for every diagnostic function indicates whether it is available in the Measurement Setup.

| Example On diagResponse Sessions::*{ char line[200]; char ecu[100]; long i; long firstCall = 1; if( this.IsPositiveResponse() == 1) write( "Positive response"); else write( "Negative response"); diagGetCurrentEcu( ecu, elcount(ecu)); DiagGetObjectPath( this, line, elcount( line)); write( "on diagResponse Sessions::*: %s from %s", line, ecu); i = 0; while( DiagGetParameterPath( this, i, line, elcount(line)) > 0) { char symbol[200]; this.GetParameter( line, symbol, elcount(symbol)); write( "%4d %-40s = %s", i++, line, symbol); } if( firstCall) { firstCall = 0; line[0] = 0; diagGetDescriptionInformation( "", line, elcount(line)); write( line); line[0] = 0; i = diagGetActiveVariant( line, elcount(line)); write( " diagGetActiveVariant (no target) returns %d and '%s'", i, line); line[0] = 0; i = diagGetConfiguredVariant( line, elcount(line)); write( " diagGetConfiguredVariant (no target) returns %d and '%s'", i, line); }output(this);} |
|---|

| Version 15© Vector Informatik GmbH |
|---|
