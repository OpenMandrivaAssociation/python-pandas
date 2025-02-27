%define	module	pandas

Summary:	Powerful Python data structures for data analysis and statistics

Name:		python-%{module}
Version:	1.5.2
Release:	2
Source0:	https://github.com/pandas-dev/pandas/releases/download/v%{version}/pandas-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://pandas.sourceforge.net/
Requires:	python-numpy >= 1.6.1
Requires:	python-dateutil
Suggests:	python-scipy
Suggests:	python-matplotlib
Suggests:	python-pytz
Suggests:	python-tables
Suggests:	python-statsmodels
BuildRequires:	pkgconfig(python)
BuildRequires:	python-cython >= 0.29.32
BuildRequires:	python-setuptools
BuildRequires:	python-numpy-devel >= 1.6.1
BuildRequires:	python-dateutil
BuildRequires:	python-matplotlib
BuildRequires:	python-sphinx
BuildRequires:	ipython
BuildRequires:	pkgconfig(lapack)

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
%autopatch -p1

%build
%__python setup.py build build_ext -lm

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
# pushd doc
# export PYTHONPATH=`dir -1d ../build/lib*`
# %__python make.py html
# find . -name .buildinfo -exec rm -rf {} \;
# popd

%files
# %doc LICENSE README.rst TODO.rst examples/ doc/build/html
%doc LICENSE
%{py_platsitedir}/%{module}*

