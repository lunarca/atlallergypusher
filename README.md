# atlantaallergypusher

This is a quick script that fetches the current pollen count in Atlanta and pushes it to a phone if the count is above 100.

It's designed to be used as a cronjob and run every morning.

## Requirements

- pyquery
- python-pushover

## Usage

This script requires the ATL_ALLERGY_PUSHOVER_API and PUSHOVER_USER_KEY to be defined in the host's environment variables.

This script is designed to be used as a chronjob that executes every morning. I recommend that you do the same.