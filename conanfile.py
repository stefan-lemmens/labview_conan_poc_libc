from conans import ConanFile

class LabVIEWBuild(ConanFile):
    python_requires = "LabVIEWConanExtension/[~=20.0.*]@intersoft/stable"
    python_requires_extend = "LabVIEWConanExtension.LabVIEWConanExtension"
    gitURL = "ssh://git@bitbucket.atlassian.inventive-engineering.com:7999/~stefan/labview_conan_poc_libc.git"
