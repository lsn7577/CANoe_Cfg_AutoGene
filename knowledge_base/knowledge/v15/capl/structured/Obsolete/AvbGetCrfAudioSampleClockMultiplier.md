# AvbGetCrfAudioSampleClockMultiplier

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Use AvbGetMediaType and query property TimestampRate using MediaGetProperty. |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Function Syntax | dword AvbGetCrfAudioSampleClockMultiplier(dword listenerOrTalkerHandle, dword& retClockMultiplier); |  |  |  |  |  |
| Function | The function retrieves the audio sample clock multiplier of the CRF stream received by the Listener or originated by the Talker. Note The nominal frequency of the audio sample clock is the clock frequency (see AvbGetCrfAudioSampleClockFrequency) multiplied by the multiplier returned by this function. | Note The nominal frequency of the audio sample clock is the clock frequency (see AvbGetCrfAudioSampleClockFrequency) multiplied by the multiplier returned by this function. |  |  |  |  |
| Note The nominal frequency of the audio sample clock is the clock frequency (see AvbGetCrfAudioSampleClockFrequency) multiplied by the multiplier returned by this function. |  |  |  |  |  |  |
| Parameters | listenerOrTalkerHandle The handle of the Listener or Talker. |  |  |  |  |  |
| retClockMultiplier The audio sample clock multiplier of the CRF stream upon successful return of the function. The following value is supported: Value Multiplier Description 0 1.0 Nominal Frequency | Value | Multiplier | Description | 0 | 1.0 | Nominal Frequency |
| Value | Multiplier | Description |  |  |  |  |
| 0 | 1.0 | Nominal Frequency |  |  |  |  |
| Return Values | 0: The function completed successfully. |  |  |  |  |  |
| >0: Error code |  |  |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |  |  |
| 8.2 SP2-9.0 SP5 | Ethernet | — | • |  |  |  |
| Example — |  |  |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
