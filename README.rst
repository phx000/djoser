Changes made
========
- Use user.<settings.USER_ID_FIELD> instead of user.pk when building magic links in emails. See: https://github.com/sunscrapers/djoser/pull/789
- On URL design:
    - Removed trailing slash from the DefaultRouter that wraps all the base views
    - Changed the urlpaths to use hyphens instead of underscores
- On logging users out on password changes:
    - Added JWT_VERSIONING=false and JWT_VERSION_FIELD="refresh_token_version" as settings
    - Made utils.logout increase the User.<JWT_VERSION_FIELD> if JWT_VERSIONING
    - Made password_reset_confirm view perform utils.logout() on success