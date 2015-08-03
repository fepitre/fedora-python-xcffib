%if 0%{?fedora} > 12
%global with_python3 1
%endif

Summary: A drop in replacement for xpyb, an XCB python binding
Name: python-xcffib
Version: 0.3.2
Release: 3%{?dist}
Source0: https://pypi.python.org/packages/source/x/xcffib/xcffib-%{version}.tar.gz
License: ASL 2.0
URL:  https://github.com/tych0/xcffib


BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  python3-setuptools
BuildRequires:  python-pycparser
BuildRequires:  python3-pycparser
BuildRequires:  libxcb-devel
BuildRequires:  python-cffi >= 1.1.2
BuildRequires:  python3-cffi >= 1.1.2
BuildRequires:  python-six
BuildRequires:  python3-six

Requires:  python-six
Requires:  python-cffi >= 1.1.2
Requires:  libxcb

%description
xcffib is intended to be a (mostly) drop-in replacement for xpyb.  xpyb
has an inactive upstream, several memory leaks, is python2 only and doesn't
have pypy support. xcffib is a binding which uses cffi, which mitigates
some of the issues described above. xcffib also builds bindings for 27 of
the 29 (xprint and xkb are missing) X extensions in 1.10.

%if 0%{?with_python3}
%package -n python3-xcffib
Summary: A drop in replacement for xpyb, an XCB python binding
Requires:  python3-six
Requires:  python3-cffi >= 1.1.2
Requires:  libxcb

%description -n python3-xcffib
xcffib is intended to be a (mostly) drop-in replacement for xpyb.  xpyb
has an inactive upstream, several memory leaks, is python2 only and doesn't
have pypy support. xcffib is a binding which uses cffi, which mitigates
some of the issues described above. xcffib also builds bindings for 27 of
the 29 (xprint and xkb are missing) X extensions in 1.10.
%endif # with_python3

%prep
%setup -q -n xcffib-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3

%build
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3

%{__python2} setup.py build


%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
popd
%endif # with_python3

%{__python2} setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES


%files
%doc LICENSE
%doc README.md
%{python2_sitelib}/xcffib
%{python2_sitelib}/xcffib*.egg-info

%if 0%{?with_python3}
%files -n python3-xcffib
%doc LICENSE
%doc README.md
%{python3_sitelib}/xcffib
%{python3_sitelib}/xcffib*.egg-info
%endif # with_python3


%changelog
* Sun Jul 12 2015 John Dulaney <jdulaney@fedoraproject.org - 0.3.2-2
- Require newer python-cffi

* Sun Jul 12 2015 John Dulaney <jdulaney@fedoraproject.org - 0.3.2-1
- Update to latest upstream

* Fri Jul 10 2015 John Dulaney <jdulaney@fedoraproject.org - 0.1.11-3
- Python3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 14 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.1.11-1
- Update to latest upstream

* Thu Jan 22 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.1.10-2
- Updated to latest version

* Tue Nov 04 2014 John Dulaney <jdulaney@fedoraproject.org> - 0.1.8-1
- Update to latest version

* Wed Oct 08 2014 John Dulaney <jdulaney@fedoraproject.org> - 0.1.7-1
- Initial packaging
- Spec based on python-nose
