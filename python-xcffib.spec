Summary: A drop in replacement for xpyb, an XCB python binding
Name: python-xcffib
Version: 0.1.8
Release: 1%{?dist}
Source0: https://pypi.python.org/packages/source/x/xcffib/xcffib-%{version}.tar.gz
License: ASL 2.0
URL:  https://github.com/tych0/xcffib

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pycparser
BuildRequires:  libxcb-devel
BuildRequires:  python-cffi
BuildRequires:  python-six

Requires:  six
Requires:  python-cffi
Requires:  libxcb

%description
xcffib is intended to be a (mostly) drop-in replacement for xpyb.  xpyb
has an inactive upstream, several memory leaks, is python2 only and doesn't
have pypy support. xcffib is a binding which uses cffi, which mitigates
some of the issues described above. xcffib also builds bindings for 27 of
the 29 (xprint and xkb are missing) X extensions in 1.10.

%prep
%setup -q -n xcffib-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%files
%doc LICENSE
%doc README.md
%{python2_sitelib}/xcffib
%{python2_sitelib}/_cffi__*
%{python2_sitelib}/xcffib*.egg-info

%changelog
* Tue Nov 04 2014 John Dulaney <jdulaney@fedoraproject.org> - 0.1.8-1
- Update to latest version

* Wed Oct 08 2014 John Dulaney <jdulaney@fedoraproject.org> - 0.1.7-1
- Initial packaging
- Spec based on python-nose
