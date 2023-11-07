Name:           cjose
Version:        0.6.1
Release:        16%{?dist}
Summary:        C library implementing the Javascript Object Signing and Encryption (JOSE)

License:        MIT
URL:            https://github.com/cisco/cjose
Source0:  	https://github.com/cisco/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

Patch1: concatkdf.patch
Patch2: 0001-Define-OPENSSL_API_COMPAT-to-0x10101000L.patch
Patch3: 0002-check-cjose_get_alloc.patch
Patch4: 0003-CVE-2023-37464.patch

BuildRequires:  gcc
BuildRequires:  doxygen
BuildRequires:  openssl-devel
BuildRequires:  jansson-devel
BuildRequires:  check-devel
BuildRequires: make

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


%ldconfig_scriptlets


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
* Wed Jul 19 2023 <thalman@redhat.com> - 0.6.1-16
- CVE-2023-37464 cjose: AES GCM decryption uses the Tag length from the actual
  Authentication Tag provided in the JWE
  Resolves: rhbz#2223308

* Wed May 3 2023 <spoore@redhat.com> - 0.6.1-15
- Rebuilt for gating
  Related: rhbz#2180445
  
* Tue May 2 2023 <thalman@redhat.com> - 0.6.1-14
- Rebuilt for gating
  Related: rhbz#2180445

* Tue Mar 21 2023 <thalman@redhat.com> - 0.6.1-13
- Random memory override
  Resolves: rhbz#2180445

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 0.6.1-12
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed Jul 28 2021 Florian Weimer <fweimer@redhat.com> - 0.6.1-11
- Rebuild to pick up OpenSSL 3.0 Beta ABI (#1984097)

* Wed Jun 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.6.1-10
- Rebuilt for RHEL 9 BETA for openssl 3.0
  Related: rhbz#1971065

* Mon May 17 2021 Jakub Hrozek <jhrozek@redhat.com> - 0.6.1-9
- enable build with openssl 3.0
- Resolves: rhbz#1958026

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 0.6.1-8
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

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
