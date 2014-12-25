import subprocess

from virtualenv.builders.base import BaseBuilder


_SCRIPT = """
import venv

# Create our actual builder with our settings.
builder = venv.EnvBuilder(
    system_site_packages={system_site_packages!r},
    clear={clear!r},
)

# Make sure that pip is actually disabled.
builder.with_pip = False

# Don't install the activate scripts, we'll want to install our own
# instead.
builder.install_scripts = lambda *a, **kw: None

# Create the virtual environment.
builder.create({destination!r})
"""


class VenvBuilder(BaseBuilder):

    @classmethod
    def check_available(self, python):
        try:
            subprocess.check_output(
                [python, "-c", "import venv"],
                stderr=subprocess.STDOUT,
            )
        except subprocess.CalledProcessError:
            return False
        else:
            return True

    def create_virtual_environment(self, destination):
        # Create our script using our template and the given settings for
        # this environment.
        script = _SCRIPT.format(
            system_site_packages=self.system_site_packages,
            clear=self.clear,
            destination=destination,
        )

        # Subshell into the venv module and create a new virtual environment.
        # We use the programatic API instead of the command line because we
        # want to not include pip in this, and Python 3.3's venv module doesn't
        # support the --without-pip flag.
        subprocess.check_call([self.python, "-c", script])