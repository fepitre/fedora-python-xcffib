Summary: A drop in replacement for xpyb, an XCB python binding
Name: python-xcffib
Version: 0.6.0
Release: 3%{?dist}
Source0: https://pypi.org/packages/source/x/xcffib/xcffib-%{version}.tar.gz
License: ASL 2.0
URL:  https://github.com/tych0/xcffib
BuildArch: noarch

BuildRequires:  libxcb-devel

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pycparser
BuildRequires:  python3-cffi >= 1.1.2
BuildRequires:  python3-six


%description
xcffib is intended to be a (mostly) drop-in replacement for xpyb.  xpyb
has an inactive upstream, several memory leaks, is python2 only and doesn't
have pypy support. xcffib is a binding which uses cffi, which mitigates
some of the issues described above. xcffib also builds bindings for 27 of
the 29 (xprint and xkb are missing) X extensions in 1.10.


%package -n python3-xcffib
Summary: A drop in replacement for xpyb, an XCB python binding
Requires:  python3-six
Requires:  python3-cffi
Requires:  libxcb

%description -n python3-xcffib
xcffib is intended to be a (mostly) drop-in replacement for xpyb.  xpyb
has an inactive upstream, several memory leaks, is python2 only and doesn't
have pypy support. xcffib is a binding which uses cffi, which mitigates
some of the issues described above. xcffib also builds bindings for 27 of
the 29 (xprint and xkb are missing) X extensions in 1.10.


%prep
%setup -q -n xcffib-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-xcffib
%doc LICENSE
%doc README.md
%{python3_sitelib}/xcffib
%{python3_sitelib}/xcffib*.egg-info


%changelog
* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.7

* Tue Mar 20 2018 John Dulaney <jdulaney@fedoraproject> - 0.6.0-2
- Drop python2 subpackage

* Fri Mar 09 2018 John Dulaney <jdulaney@fedoraproject> - 0.6.0-1
- Update to latest release

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.1-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.1-4
- Fix creation of python2- subpackage

* Thu Aug 10 2017 John Dulaney <jdulaney@fedoraproject.org> - 0.5.1-2
- Modernize spec file a bit, including expressly build python2- binary package

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 06 2017 John Dulaney <jdulaney@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-2
- Rebuild for Python 3.6

* Fri May 06 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Fri Feb 12 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.4.1-1
- Update to latest upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

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
