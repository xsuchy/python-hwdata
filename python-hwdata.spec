%if (0%{?fedora} || 0%{?rhel} > 6)
%global with_python3 1
%else
%global with_python3 0
%endif

Name:		python-hwdata
Version:	2.3.5
Release:	1%{?dist}
Summary:	Python bindings to hwdata package
BuildArch:  noarch
License:	GPLv2
URL:		https://github.com/xsuchy/python-hwdata
# git clone https://github.com/xsuchy/python-hwdata.git
# cd python-hwdata
# tito build --tgz
Source0:	%{name}-%{version}.tar.gz

BuildRequires: python-devel

%description
Provide python interface to database stored in hwdata package.
It allows you to get human readable description of USB and PCI devices.

%package -n python2-hwdata
Summary:	Python bindings to hwdata package
Requires:	hwdata
%{?python_provide:%python_provide python2-hwdata}
%if 0%{?rhel} < 8
Provides:	python-hwdata = %{version}-%{release}
%endif

%description -n python2-hwdata
Provide python interface to database stored in hwdata package.
It allows you to get human readable description of USB and PCI devices.

This is the Python 2 build of the module.

%if 0%{?with_python3}
%package -n python3-hwdata
Summary:	Python bindings to hwdata package

BuildRequires:	python3-devel
BuildRequires:	python3-pylint
Requires:	hwdata

%description -n python3-hwdata
Provide python interface to database stored in hwdata package.
It allows you to get human readable description of USB and PCI devices.

This is the Python 3 build of the module.
%endif

%prep
%setup -q

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%{__python} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}
popd
%endif

%check
%if 0%{?with_python3}
pylint-3 hwdata.py example.py || :
%endif

%files -n python2-hwdata
%license LICENSE
%doc README.md example.py
%doc html
%{python_sitelib}/*

%if 0%{?with_python3}
%files -n python3-hwdata
%license LICENSE
%doc README.md example.py
%doc html
%{python3_sitelib}/*
%endif

%changelog
* Wed Aug 09 2017 Miroslav Suchý <msuchy@redhat.com> 2.3.5-1
- create python2-hwdata subpackage
- use dnf instead of yum in README
- remove rhel5 compatibilities from spec

* Thu Sep 22 2016 Miroslav Suchý <miroslav@suchy.cz> 2.3.4-1
- run pylint in %%check
- require hwdata in python 3 package too (jdobes@redhat.com)
- implement PNP interface
- errors in usb.ids should not be fatal
- change upstream url in setup.py

* Wed Jan 28 2015 Miroslav Suchý <msuchy@redhat.com> 2.3.3-1
- upstream location changed

* Wed Jan 28 2015 Miroslav Suchý <msuchy@redhat.com>
- move upstream location

* Wed Dec 04 2013 Miroslav Suchý <msuchy@redhat.com> 1.10.1-1
- create python3-hwdata subpackage
- Bumping package versions for 1.9
- %%defattr is not needed since rpm 4.4

* Fri Mar 02 2012 Miroslav Suchý 1.7.3-1
- 798375 - fix PCI device name translation (Joshua.Roys@gtri.gatech.edu)
- use setup from distutils

* Fri Mar 02 2012 Jan Pazdziora 1.7.2-1
- Update the copyright year info.

* Fri Mar 02 2012 Jan Pazdziora 1.7.1-1
- correct indentation (mzazrivec@redhat.com)

* Mon Oct 31 2011 Miroslav Suchý 1.6.2-1
- point URL to specific python-hwdata page

* Fri Jul 22 2011 Jan Pazdziora 1.6.1-1
- We only support version 14 and newer of Fedora, removing conditions for old
  versions.

* Mon Apr 26 2010 Miroslav Suchý <msuchy@redhat.com> 1.2-1
- 585138 - change %%files section and patial support for python3

* Fri Apr 23 2010 Miroslav Suchý <msuchy@redhat.com> 1.1-1
- initial release
