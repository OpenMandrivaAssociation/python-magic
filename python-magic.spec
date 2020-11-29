%global pypi_name python-magic

Name:           %{pypi_name}
Version:        0.4.18
Release:        1
Summary:        File type identification using libmagic
Group:          Development/Python
License:        MIT
URL:            https://github.com/ahupp/python-magic
Source0:        https://github.com/ahupp/python-magic/archive/%{version}/%{pypi_name}-%{version}.tar.gz
Patch0:         python-magic-git-Fix-tests-with-file-5.39.patch

BuildArch:      noarch

%description
This module uses ctypes to access the libmagic file type identification
library. It makes use of the local magic database and supports both textual
and MIME-type output.

%package -n     python-%{pypi_name}
Summary:        File type identification using libmagic
Group:          Development/Python

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
# For tests.
BuildRequires:  locales-en

Provides:       python-magic = %{version}-%{release}
Provides:       python3-magic = %{version}-%{release}
Conflicts:      python3-magic < 5.39-2
Conflicts:      python-magic < 5.39-2
Conflicts:      python-file

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py_build

%install
%py_install

%check
export LC_ALL=en_US.UTF-8
export PYTHONPATH=.
%{__python3} test/test.py

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/__pycache__/magic.*
%{python3_sitelib}/magic.py
%{python3_sitelib}/python_magic-%{version}-py*.egg-info
