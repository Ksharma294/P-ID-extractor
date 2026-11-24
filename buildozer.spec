[app]

# (str) Title of your application
title = P&ID Extractor

# (str) Package name
package.name = pidextractor

# (str) Package domain (needed for android/ios packaging)
package.domain = org.pid

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,pdf

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec,txt,md,yml,apk

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin, .buildozer, .github

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# Kivy is the UI, PyMuPDF reads the PDF files
requirements = python3,kivy==2.3.0,pymupdf

# (str) Presplash of the Application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the Application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0


#
# Android specific
#

# (list) Permissions
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, READ_MEDIA_IMAGES

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (list) Android application meta-data to set (key=value format)
# android.meta_data =

# (list) Android additional libraries to copy into libs/armeabi
# android.add_libs_armeabi = libs/android/*.so
# android.add_libs_armeabi_v7a = libs/android-v7/*.so
# android.add_libs_arm64_v8a = libs/android-v8/*.so

# (list) Pattern to whitelist the application for Android 9+ (cleartext traffic)
# android.whitelist =

# (str) Android app theme, default is ok for Kivy
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (bool) Enable AndroidX support.
android.enable_androidx = True

# (list) List of Java .jar files to add to the libs
# android.add_jars = foo.jar,bar.jar

# (list) List of Java files to add to the android project
# android.add_src = src

# (list) Android AAR archives to add
# android.add_aars =

# (bool) Use --private data storage (True) or --dir public storage (False)
# android.private_storage = True


#
# Python for android (p4a) specific
#

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
# p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes
# p4a.local_recipes =

# (str) Filename to the hook for p4a
# p4a.hook =

# (str) Bootstrap to use for android builds (sdl2 is default)
# p4a.bootstrap = sdl2

# (int) port number to use for the debug server
# p4a.port = 5000

# (str) Branch of p4a to use (default is master)
p4a.branch = master


#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
# ios.kivy_ios_dir = ../kivy-ios

# (str) Name of the certificate to use for signing the debug version
# ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) Name of the certificate to use for signing the release version
# ios.codesign.release = %(ios.codesign.debug)s


#
# Buildozer specific
#

# (str) Log level: 0=all, 1=debug, 2=info, 3=warn, 4=error, 5=critical
log_level = 2

# (str) Warning on the console if the requirements are not installed
warn_on_root = 1

# (list) List of change order operation
# buildops = 

# (str) Path to build artifact storage
# build_dir = ./.buildozer

# (str) Path to test files
# bin_dir = ./bin

# (list) List of environment variable to set
# buildozer_env = 

# (str) JSON file to update
# json = 

# (str) Path to cache directory
# cache_dir = ./.cache

# (str) Path to the Android SDK
# android.sdk_path =

# (str) Path to the Android NDK
# android.ndk_path =

# (str) Path to Ant
# android.ant_path =

# (str) Path to the Android update tool
# android.update_tool_path =

# (str) Path to the Android Adb tool
# android.adb_path =