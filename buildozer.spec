[app]
title = P&ID Extractor
package.name = pidextractor
package.domain = org.pid
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,pdf
source.exclude_exts = spec,txt,md,yml,apk
source.exclude_dirs = tests, bin, .buildozer, .github
version = 1.0.0
requirements = python3,kivy==2.3.0,pypdf
orientation = portrait
fullscreen = 0
android.accept_sdk_license = True
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, READ_MEDIA_IMAGES
android.api = 33
android.minapi = 24
android.sdk = 33
android.ndk = 25b
p4a.branch = master
