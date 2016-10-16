# Check Versions
_The project to check your project's requirements._

## README
- [ENGLISH](README.md) || [PORTUGUÊS](README-ptbr.md)

## What`s it?

 - This project is a better way to see your requirements security with [requires.io](http://requires.io) API
 - This project is a dashboard to know how updated your requirements.

## SETTINGS

Required edit file [settings.yaml](settings.yaml)

### settings.yaml

**requires.io**
```yaml
REQUIRES_IO:
    ACTIVE: True || False # This config is to activate or desactivate the requires.io
    SECURITY_TOKEN: False || True # this config is to using os environ token.
    USER: PUT_HERE_YOUR_USER # requires.io's user
    TOKEN: PUT_HERE_YOUR_TOKEN # requires.io's token if not using SECURITY_TOKEN
    REPOSITORY_NAME: PUT_HERE_YOUR_REPOSITORY_NAME # requires.io's repository name
    UGLIFY_REPOSITORY: False || TRUE # This config is to hide the name of project, userful in project can't identified in free plan on requires.io
    REPOSITORY_BRANCH: master # requires.io's branch
```

**Project requirements**
```yaml
PROJECT:
  NAME: PUT_HERE_THE_PROJECT_NAME # Project's name.
  REQUIREMENTS_TYPE: txt || json # requirements's format type.
  REQUIREMENTS_URL: PUT_HERE_THE_URL # requirements's URL.
```

