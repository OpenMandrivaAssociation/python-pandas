%define	module	pandas

Summary:	Powerful Python data structures for data analysis and statistics

Name:		python-%{module}
Version:	2.3.3
Release:	1
Source0:	https://github.com/pandas-dev/pandas/releases/download/v%{version}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
URL:		https://github.com/pandas-dev/pandas
BuildSystem:	meson
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(cython) >= 0.29.32
BuildRequires:	python%{pyver}dist(matplotlib)
BuildRequires:	python%{pyver}dist(meson-python)
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	python%{pyver}dist(python-dateutil)
BuildRequires:	python%{pyver}dist(pytz)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(tzdata)
BuildRequires:	python%{pyver}dist(versioneer)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python-sphinx
BuildRequires:	ipython
BuildRequires:	pkgconfig(lapack)
Requires:	python%{pyver}dist(numpy)
Requires:	python%{pyver}dist(python-dateutil)
Requires:	python%{pyver}dist(pytz)
Requires:	python%{pyver}dist(tzdata)
Suggests:	python%{pyver}dist(scipy)
Suggests:	python%{pyver}dist(matplotlib)
Suggests:	python%{pyver}dist(pytz)
Suggests:	python%{pyver}dist(tables)
Suggests:	python%{pyver}dist(statsmodels)

%description
pandas is a Python package providing fast, flexible, and expressive
data structures designed to make working with "relational" or
"labeled" data both easy and intuitive. It aims to be the fundamental
high-level building block for doing practical, real world data
analysis in Python. Additionally, it has the broader goal of becoming
the most powerful and flexible open source data analysis /
manipulation tool available in any language. It is already well on its
way toward this goal.

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{ldflags} -lpython%{py_ver}"
%py_build

%files
%doc README.md
%license LICENSE LICENSES/
%{py_platsitedir}/%{module}/*
