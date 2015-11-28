#
# TODO:
#	- Assetrion error at "guppy/heapy/Part.py", line 705, in __init__
#	  when used interactively
#
%define 	module	guppy
Summary:	Guppy - A Python Programming Environment
Name:		python-%{module}
Version:	0.1.9
Release:	2
License:	MIT
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/g/guppy/%{module}-%{version}.tar.gz
# Source0-md5:	221c50d574277e4589cc4ae03f76727a
Patch0:		%{name}-python_2_7.patch
URL:		http://guppy-pe.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Guppy-PE is a programming environment providing object and heap memory
sizing, profiling and analysis. It includes a prototypical
specification language that can be used to formally specify aspects of
Python programs and generate tests and documentation from a common
source.

Guppy is an umbrella package combining Heapy and GSL with support
utilities such as the Glue module that keeps things together.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE ChangeLog README PKG-INFO
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/doc
%{py_sitedir}/%{module}/doc/*.html
%{py_sitedir}/%{module}/doc/*.jpg
%dir %{py_sitedir}/%{module}%{_sysconfdir}
%dir %{py_sitedir}/%{module}/gsl
%dir %{py_sitedir}/%{module}/heapy
%dir %{py_sitedir}/%{module}/heapy/test
%dir %{py_sitedir}/%{module}/sets
%{py_sitedir}/%{module}/*/*.py[co]
%{py_sitedir}/%{module}/*/test/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/*/*.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/%{module}-*.egg-info
%endif
