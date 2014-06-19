# Copyright (C) Ivan Kravets <me@ikravets.com>
# See LICENSE for details.

from click import argument, command, option, secho

from platformio.platforms._base import PlatformFactory


@command("install", short_help="Install new platforms")
@argument("platforms", nargs=-1)
@option('--with-package', multiple=True, metavar="<package>")
@option('--without-package', multiple=True, metavar="<package>")
def cli(platforms, with_package, without_package):

    for platform in platforms:

        p = PlatformFactory().newPlatform(platform)

        if p.install(with_package, without_package):
            secho("The platform '%s' has been successfully installed!" %
                  platform, fg="green")
