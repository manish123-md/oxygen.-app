[app]

# (string) Title of your application
title = Oxygen

# (string) Package name
package.name = oxygen

# (string) Package domain (needed for android package name)
package.domain = org.desigen2code

# (string) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (string) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# ==============================================================================
# Android specific configurations
# ==============================================================================

# (int) Android API to use
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 24

# (str) Android NDK version to use (Locked to stable 25c to prevent crashes!)
android.ndk = 25c

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow nighttime or automatic cleanups
android.skip_update = False

# (int) loglevel for the buildozer output (2 = traditional, 1 = info, 0 = error)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (default))
log_level = 2

# (str) Path to build artifacts
bin_dir = ./bin
