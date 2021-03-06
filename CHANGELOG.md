# v0.4: 18 September 2018

- Split dataset and user APIs to clarify our API structure, and get ready for
future extensions.

# v0.3: 14 August 2018

- CaptureLog now takes a start and end timestamp. Please note that since the
  order here is reverse chronological, the start timestamp is the most recent
  time, and the end timestamp is the least recent time.
- Add the tempdownload command, which downloads a temporary capture's assets to
  a local directory.
- The netograph library is now available on the official PyPi registry. You can
  install it with `pip install netograph` without checking out this repo.

# v0.2: 27 July 2018

- RedirsBySource/RedirsByDestination: search redirections by source and
  destination domain queries.
- TempCapture: request a temporary capture. Temporary captures are not loaded
  into datasets. Download assets expire in 24 hours.
- SubmitCapture now returns the capture ID as a separate field.

# v0.1: 16 July 2018

- Initial release
