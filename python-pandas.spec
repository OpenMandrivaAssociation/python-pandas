%define	module	pandas

Summary:	Powerful Python data structures for data analysis and statistics
Name:		python-%{module}
Version:	0.8.1
Release:	2
Source0:	http://pypi.python.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
Patch0:		setup-lm-0.8.0.patch
Patch1:		make-doc-0.8.0.patch
License:	BSD
Group:		Development/Python
Url:		http://pandas.sourceforge.net/
Requires:	python-numpy >= 1.6.1
Requires:	python-dateutil < 2
Suggests:	python-scipy
Suggests:	python-matplotlib
Suggests:	python-pytz
Suggests:	python-tables
Suggests:	python-statsmodels
BuildRequires:	python-setuptools
BuildRequires:	python-numpy-devel >= 1.6.1
BuildRequires:	python-dateutil < 2
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
%patch0 -p0
%patch1 -p0

%build
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
pushd doc
export PYTHONPATH=`dir -1d ../build/lib*`
%__python make.py html
find . -name .buildinfo -exec rm -rf {} \;
popd

%files
%doc LICENSE README.rst TODO.rst examples/ doc/build/html
%py_platsitedir/%{module}*


%changelog
* Mon Jul 30 2012 Lev Givon <lev@mandriva.org> 0.8.1-1
+ Revision: 811490
- Update to 0.8.1.

* Mon Jul 02 2012 Lev Givon <lev@mandriva.org> 0.8.0-1
+ Revision: 807858
- Update to 0.8.0 final.

* Tue Jun 26 2012 Lev Givon <lev@mandriva.org> 0.8.0-0.rc2
+ Revision: 806941
- imported package python-pandas

