# Check Versions
_Keep your dependencies in check_

## README
- **ENGLISH** || [PORTUGUÊS](README-ptbr.md)

## What's this?

 - A better way to keep your dependencies security in check with [requires.io](http://requires.io) API
 - A dashboard to know if your project's dependencies are up to date.

## SETTINGS

To run this service, edit [settings.yaml](settings.yaml)

### settings.yaml

**requires.io**
```yaml
REQUIRES_IO:
    ACTIVE: True || False # Activate or deactivate requires.io checks
    SECURITY_TOKEN: False || True # If True, Check Versions will get the token from environment.
    USER: PUT_HERE_YOUR_USER # requires.io user
    TOKEN: PUT_HERE_YOUR_TOKEN # requires.io token, if SECURITY_TOKEN is False
    REPOSITORY_NAME: PUT_HERE_YOUR_REPOSITORY_NAME # requires.io repository name
    UGLIFY_REPOSITORY: False || True # Hide the name of your project on requires.io
    REPOSITORY_BRANCH: master # requires.io branch
```

**Project requirements**
```yaml
PROJECT:
  NAME: PUT_HERE_THE_PROJECT_NAME # Project's name.
  REQUIREMENTS_TYPE: txt || json # requirements' format type.
  REQUIREMENTS_URL: PUT_HERE_THE_URL # requirements' URL.
```

