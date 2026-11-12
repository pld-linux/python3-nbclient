#
# Conditional build:
%bcond_with	tests	# unit tests (TODO: complete dependencies in PLD)

%define 	module	nbclient
Summary:	A client library for executing notebooks
Summary(pl.UTF-8):	Biblioteka kliencka do wykonywania notebooków
Name:		python3-%{module}
Version:	0.11.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/nbclient/
Source0:	https://files.pythonhosted.org/packages/source/n/nbclient/%{module}-%{version}.tar.gz
# Source0-md5:	d927c9d65c9c7828f09855ed7f052c5b
URL:		https://jupyter.org/
BuildRequires:	python3-build
BuildRequires:	python3-hatchling >= 1.10.0
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10.0
%if %{with tests}
BuildRequires:	python3-flaky
BuildRequires:	python3-ipykernel >= 6.19.3
BuildRequires:	python3-ipython
BuildRequires:	python3-ipywidgets
BuildRequires:	python3-jupyter_client >= 7.0.0
BuildRequires:	python3-jupyter_core >= 5.4.0
BuildRequires:	python3-nbconvert >= 7.1.0
BuildRequires:	python3-nbformat >= 5.2.0
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-asyncio >= 1.3.0
BuildRequires:	python3-testpath
BuildRequires:	python3-traitlets >= 5.13
BuildRequires:	python3-xmltodict
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A client library for executing notebooks.

%description -l pl.UTF-8
Biblioteka kliencka do wykonywania notebooków.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_asyncio.plugin \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/jupyter-execute
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
