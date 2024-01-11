Name:           cjose
Version:        0.6.1
Release:        4%{?dist}
Summary:        C library implementing the Javascript Object Signing and Encryption (JOSE)

License:        MIT
URL:            https://github.com/cisco/cjose
Source0:  	https://github.com/cisco/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

Patch1: concatkdf.patch
Patch2: 0002-check-cjose_get_alloc.patch
Patch3: 0003-CVE-2023-37464.patch

BuildRequires:  gcc
BuildRequires:  doxygen
BuildRequires:  openssl-devel
BuildRequires:  jansson-devel
BuildRequires:  check-devel

%description
Implementation of JOSE for C/C++


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure
%make_build


%install
%make_install
find %{buildroot} -name '*.a' -exec rm -f {} ';'
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%check
make check || (cat test/test-suite.log; exit 1)

%files
%license LICENSE
%doc CHANGELOG.md README.md
%doc /usr/share/doc/cjose
%{_libdir}/*.so.*


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/cjose.pc


%changelog
* Wed Jul 19 2023 <thalman@redhat.com> - 0.6.1-4
- CVE-2023-37464 cjose: AES GCM decryption uses the Tag length from the actual
  Authentication Tag provided in the JWE
  Resolves: rhbz#2223308

* Fri Mar 17 2023 <thalman@redhat.com> - 0.6.1-3
- Random memory override
  Resolves: rhbz#2072469

* Thu Aug  2 2018  <jdennis@redhat.com> - 0.6.1-2
- fix concatkdf big endian architecture problem.
  Upstream issue #77.

* Wed Aug  1 2018  <jdennis@redhat.com> - 0.6.1-1
- upgrade to latest upstream 0.6.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Patrick Uiterwijk <patrick@puiterwijk.org> - 0.5.1-1
- Initial packaging
