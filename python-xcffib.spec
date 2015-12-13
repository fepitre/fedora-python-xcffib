%if 0%{?fedora}
%global with_python3 1
%endif

Summary: A drop in replacement for xpyb, an XCB python binding
Name: python-xcffib
Version: 0.4.0
Release: 3%{?dist}
Source0: https://pypi.python.org/packages/source/x/xcffib/xcffib-%{version}.tar.gz
License: ASL 2.0
URL:  https://github.com/tych0/xcffib
BuildArch: noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pycparser
BuildRequires:  libxcb-devel
BuildRequires:  python-cffi >= 1.1.2
BuildRequires:  python-six

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pycparser
BuildRequires:  python3-cffi >= 1.1.2
BuildRequires:  python3-six
%endif

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
%py2_build
%if 0%{?with_python3}
%py3_build
%endif # with_python3



%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif # with_python3


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
* Sun Dec 13 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.4.0-3
- Rebuild against new cffi

* Thu Nov 19 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.4.0-2
- Prepare for epel

* Thu Nov 19 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.4.0-1
- Update to latest upstream

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6-1
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct 19 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.3.6-1
- Update to latest upstream

* Mon Oct 19 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.3.2-5
- Rebuild against newest python-cairocffi (bz #1249821)

* Mon Aug 03 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.3.2-4
- Switch to noarch as no longer shipping C code

* Sun Jul 12 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.3.2-2
- Require newer python-cffi

* Sun Jul 12 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.3.2-1
- Update to latest upstream

* Fri Jul 10 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.1.11-3
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
