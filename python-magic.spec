Name:		python-magic
Version:	0.4.27
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/p/python-magic/python-magic-%{version}.tar.gz
Summary:	Determines a file's mime type by its magic number
URL:		https://pypi.org/project/magic/
License:	GPL
Group:		Development/Python
BuildArch:	noarch
BuildRequires:	python
BuildSystem:	python

%description
Determines a file's mime type by its magic number

%files
%{py_sitedir}/magic
%{py_sitedir}/python_magic-*.*-info
