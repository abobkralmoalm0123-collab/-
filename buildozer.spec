[app]
# (str) Title of your application
title = Omega Alpha Quantum X

# (str) Package name
package.name = omega_alpha

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# هنا بنضيف المكاتب اللي الـ AI بيحتاجها عشان ميحصلش حظر
requirements = python3,kivy,requests,fake-useragent,urllib3

# (list) Permissions
# دي أهم حتة: صلاحيات الإنترنت، التخزين، والتحكم العميق
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, SYSTEM_ALERT_WINDOW, ACCESS_FINE_LOCATION

# (int) Android API to use (33 is stable for Android 13+)
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use the private storage for the application
android.private_storage = True

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Architecture to build for (Standard for most phones)
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
