The Better Bioinformatics Software Society (TBBSS): https://github.com/TBBSS
============================================================================

Mitchell Stanton-Cook (m.stantoncook@gmail.com) is using your code in a project.

He noticed you were not tagging releases. He's provided you with a script 
**do_release.sh**.

It depends on -
   * (pip)
   * bumpversion
   * wheel
   * twine 

You can install the using::

    $ pip install -r requirements-dev.txt


Using do_release.sh
-------------------

Set the following in your (BASH shell)::

    export VERSION=0.1.6
    export BUMP_TYPE=patch
    # can be major, minor, patch. See http://semver.org
    export PYPIUSER=user
    export PYPIPASS=pass
    # Above assumes- have PyPI account and have registered you project
    # see: http://peterdowns.com/posts/first-time-with-pypi.html


**Note:** See *.bumpversion.cfg* for finer control.

Finally::

    ./do_release.sh

In this case::

    export VERSION=0.1.6
    export BUMP_TYPE=patch
    export PYPIUSER=user
    export PYPIPASS=pass
    sh do_release.sh

Generated:
    * https://github.com/TBBSS/rubra/releases/tag/v0.1.6 and 
    * (would have updated PyPI version as well...)


Cheers ;-)
