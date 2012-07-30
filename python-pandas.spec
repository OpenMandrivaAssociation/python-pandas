%define	module	pandas
%define name	python-%{module}
%define version 0.8.1
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release	%{rel}
%endif

Summary:	Powerful Python data structures for data analysis and statistics
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
Patch0:		setup-lm-0.8.0.patch
Patch1:		make-doc-0.8.0.patch
License:	BSD
Group:		Development/Python
Url:		http://pandas.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python-numpy >= 1.6.1
Requires:	python-dateutil < 2
Suggests:	python-scipy, python-matplotlib, python-pytz, python-tables, python-statsmodels
BuildRequires:	python-setuptools
BuildRequires:	python-numpy-devel >= 1.6.1
BuildRequires:	python-dateutil < 2
BuildRequires:	python-sphinx

%description
pandas is a Python package providing fast, flexible, and expressive
data structures designed to make working with "relational" or
"labeled" data both easy and intuitive. It aims to be the fundamental
high-level building block for doing practical, real world data
analysis in Python. Additionally, it has the broader goal of becoming
the most powerful and flexible open source data analysis /
manipulation tool available in any language. It is already well on its
way toward this goal.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0
%patch1 -p0

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
pushd doc
export PYTHONPATH=`dir -1d ../build/lib*`
%__python make.py html
find . -name .buildinfo -exec rm -rf {} \;
popd

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README.rst TODO.rst examples/ doc/build/html
%py_platsitedir/%{module}*
