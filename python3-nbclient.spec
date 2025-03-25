
%define 	module	nbclient
Summary:	A client library for executing notebooks
Name:		python3-%{module}
Version:	0.10.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/nbclient/
Source0:	https://files.pythonhosted.org/packages/source/n/nbclient/%{module}-%{version}.tar.gz
# Source0-md5:	f946a5301693923eb4084ef59aaa0233
URL:		https://jupyter.org/
BuildRequires:	python3-build
BuildRequires:	python3-hatchling >= 1.10.0
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A client library for executing notebooks.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

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
