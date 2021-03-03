# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
from os import environ as env

ENVIRONMENT_URLS = {
    "production": {
        "authentication": env.get("PROD_AUTH_URL", "https://api.accounts.firefox.com/v1"),
        "oauth": env.get("PROD_OAUTH_URL", "https://oauth.accounts.firefox.com/v1"),
        "content": env.get("PROD_CONTENT_URL", "https://accounts.firefox.com/"),
        "profile": env.get("PROD_PROFILE_URL", "https://profile.accounts.firefox.com/v1"),
        "token": env.get("PROD_TOKEN_URL", "https://token.services.mozilla.com/"),
    },
    "stage": {
        "authentication": env.get("STAGE_AUTH_URL", "https://api-accounts.stage.mozaws.net/v1"),
        "oauth": env.get("STAGE_OAUTH_URL", "https://oauth.stage.mozaws.net/v1"),
        "content": env.get("STAGE_CONTENT_URL", "https://accounts.stage.mozaws.net/"),
        "profile": env.get("STAGE_PROFILE_URL", "https://profile.stage.mozaws.net/v1"),
        "token": env.get("STAGE_TOKEN_URL", "https://token.stage.mozaws.net/"),
    },
    "stable": {
        "authentication": env.get("STABLE_AUTH_URL", "https://stable.dev.lcip.org/auth/v1"),
        "oauth": env.get("STABLE_OAUTH_URL", "https://oauth-stable.dev.lcip.org/v1"),
        "content": env.get("STABLE_CONTENT_URL", "https://stable.dev.lcip.org/"),
        "profile": env.get("STABLE_PROFILE_URL", "https://stable.dev.lcip.org/profile/v1"),
        "token": env.get("STABLE_TOKEN_URL", None),
    }
}

PRODUCTION_URLS = ENVIRONMENT_URLS['production']
STAGE_URLS = ENVIRONMENT_URLS['stage']
STABLE_URLS = ENVIRONMENT_URLS['stable']
